from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Club


# Create your views here.

class ClubList(generic.ListView):
    queryset = Club.objects.filter(status=1).annotate(approved_count=Count('approved_members'))
    template_name = "club/clubs.html"
    paginate_by = 6


def club_detail(request, slug):
    """
    Display an individual :model:`club.Club`.
    """

    queryset = Club.objects.filter(status=1)
    club = get_object_or_404(queryset, slug=slug)
    return render(request, 'club_detail.html', {
        'club': club,
    })
