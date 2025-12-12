from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Club
from .forms import ClubForm

# Create your views here.

class ClubList(generic.ListView):
    queryset = Club.objects.filter(is_private=False).annotate(approved_count=Count('approved_members'))
    template_name = "club/clubs.html"
    paginate_by = 6


def club_detail(request, slug):
    """
    Display an individual :model:`club.Club`.
    """
    queryset = Club.objects.filter(status=1)
    club = get_object_or_404(queryset, slug=slug)
    return render(request, 'club/club_detail.html', {
        'club': club,
    })

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
            return redirect('clubs')  # or wherever you want to go after creation
    else:
        form = ClubForm()
    return render(request, 'club/create.html', {'form': form})
