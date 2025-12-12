from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.contrib import messages

from .forms import ClubForm
from .models import Club

# Create your views here.


class ClubList(LoginRequiredMixin, generic.ListView):
    login_url = settings.LOGIN_URL
    queryset = Club.objects.filter(is_private=False).annotate(
        approved_count=Count('approved_members'))
    template_name = "club/clubs.html"
    paginate_by = 6


@login_required(login_url=settings.LOGIN_URL)
def club_detail(request, slug):
    """
    Display an individual :model:`club.Club`.
    """
    queryset = Club.objects.filter(is_private=False).annotate(
        approved_count=Count('approved_members'))
    club = get_object_or_404(queryset, slug=slug)
    context = {'club': club}
    # Provide edit form only to owner (for modal editing)
    if request.user == club.author:
        context['club_form'] = ClubForm(instance=club)
    return render(request, 'club/club_detail.html', context)


@login_required(login_url=settings.LOGIN_URL)
def club_create(request):
    """
    Show the form for creating a new :model:`club.Club`.
    """
    if request.method == 'POST':
        form = ClubForm(request.POST)
        if form.is_valid():
            club = form.save(commit=False)
            club.author = request.user
            club.save()
            # Add creator as an approved member and redirect to list
            club.approved_members.add(request.user)
            return redirect('clubs')
    else:
        form = ClubForm()
    return render(request, 'club/create.html', {'form': form})


@login_required(login_url=settings.LOGIN_URL)
def my_clubs(request):
    """List clubs created by the user and clubs they've joined (approved)."""
    my_created = (
        Club.objects.filter(author=request.user)
        .annotate(approved_count=Count('approved_members'))
        .order_by('-created_on')
    )
    my_joined = (
        Club.objects.filter(approved_members=request.user)
        .exclude(author=request.user)
        .annotate(approved_count=Count('approved_members'))
        .order_by('-created_on')
    )
    my_pending = (
        Club.objects.filter(unapproved_members=request.user)
        .annotate(approved_count=Count('approved_members'))
        .order_by('-created_on')
    )
    return render(request, 'club/my_clubs.html', {
        'my_created': my_created,
        'my_joined': my_joined,
        'my_pending': my_pending,
    })


@login_required(login_url=settings.LOGIN_URL)
def club_join(request, slug):
    """Allow a logged-in user to join a club.
    - If approval required, add to unapproved_members (waitlist)
    - Else add directly to approved_members
    """
    if request.method != 'POST':
        messages.warning(
            request, 'Join cancelled. Please use the Join button to submit your request.')
        return redirect('club_detail', slug=slug)

    club = get_object_or_404(Club, slug=slug)

    # Already a member or in waitlist
    if request.user in club.approved_members.all():
        messages.info(
            request, 'You are already an approved member of this club.')
        return redirect('club_detail', slug=slug)
    if request.user in club.unapproved_members.all():
        messages.info(request, 'Your request is pending approval.')
        return redirect('club_detail', slug=slug)

    if club.require_approval:
        club.unapproved_members.add(request.user)
        messages.success(
            request, 'Request sent. The organizer must approve your membership.')
    else:
        club.approved_members.add(request.user)
        messages.success(request, 'You have joined the club successfully!')
    return redirect('club_detail', slug=slug)


@login_required(login_url=settings.LOGIN_URL)
def club_update(request, slug):
    """Allow the club owner to update club details via modal (Crispy form)."""
    club = get_object_or_404(Club, slug=slug)
    if request.user != club.author:
        return HttpResponseForbidden("You do not have permission to edit this club.")

    if request.method == 'POST':
        form = ClubForm(request.POST, instance=club)
        if form.is_valid():
            form.save()
            messages.success(request, 'Club details updated successfully.')
            return redirect('club_detail', slug=slug)
    else:
        form = ClubForm(instance=club)

    # Fallback page render if modal-post returns validation errors
    return render(request, 'club/club_detail.html', {
        'club': club,
        'club_form': form,
    })


@login_required(login_url=settings.LOGIN_URL)
def club_delete(request, slug):
    """Allow the club owner to delete their club after confirmation.
    Requires POST with field `confirm_text` equal to 'I understand'.
    """
    club = get_object_or_404(Club, slug=slug)
    if request.user != club.author:
        return HttpResponseForbidden("You do not have permission to delete this club.")

    if request.method != 'POST':
        return redirect('club_detail', slug=slug)

    confirm_text = request.POST.get('confirm_text', '')
    if confirm_text.strip() != 'I understand':
        messages.error(
            request, "Deletion failed: You must type 'I understand' exactly.")
        return redirect('club_detail', slug=slug)

    title = club.title
    club.delete()
    messages.success(request, f'Club "{title}" was deleted successfully.')
    return redirect('my_clubs')
