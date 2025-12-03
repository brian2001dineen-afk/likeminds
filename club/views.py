from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Club


# Create your views here.

class ClubList(generic.ListView):
    queryset = Club.objects.filter(status=1)
    template_name = "club/clubs.html"
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        clubs = context['object_list']
        # Add approved member counts for each club
        context['approved_counts'] = {club.id: club.approved_members.count() for club in clubs}
        # Or, to access approved members themselves:
        # context['approved_members'] = {club.id: club.approved_members.all() for club in clubs}
        return context

def club_detail(request, slug):
    """
    Display an individual :model:`club.Club`.
    """

    queryset = Club.objects.filter(status=1)
    club = get_object_or_404(queryset, slug=slug)
    approved_counts = club.approved_members.count()
    return render(request, 'club_detail.html', {
        'club': club,
        'approved_counts': approved_counts,
    })
