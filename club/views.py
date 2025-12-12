from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import ClubForm
from .models import Club

# Create your views here.

class ClubList(LoginRequiredMixin, generic.ListView):
    login_url = settings.LOGIN_URL
    queryset = Club.objects.filter(is_private=False).annotate(approved_count=Count('approved_members'))
    template_name = "club/clubs.html"
    paginate_by = 6

@login_required(login_url=settings.LOGIN_URL)
def club_detail(request, slug):
    """
    Display an individual :model:`club.Club`.
    """
    queryset = Club.objects.filter(status=1)
    club = get_object_or_404(queryset, slug=slug)
    return render(request, 'club/club_detail.html', {
        'club': club,
    })

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
            club.approved_members.add(request.user)  # Add creator as an approved member
            club.save()
            return redirect('clubs')  # or wherever you want to go after creation
    else:
        form = ClubForm()
    return render(request, 'club/create.html', {'form': form})
