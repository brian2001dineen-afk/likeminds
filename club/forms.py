from .models import Club
from django import forms


class ClubForm(forms.ModelForm):
    """
    Creates a club form for creating and updating club instances.
    """
    class Meta:
        model = Club
        fields = [
            'name',
            'excerpt',
            'organizer_name',
            'organizer_email',
            'personal_intro',
            'club_briefing',
            'prerequisites',
            'expectations',
            'schedule_description',
            'max_members',
            'is_private',
            'require_approval',
        ]
