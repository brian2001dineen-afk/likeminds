from .models import Club
from django import forms


class ClubForm(forms.ModelForm):
    """
    Creates a form for :model:`blog.Comment` to create comments
    """
    class Meta:
        model = Club
        fields = ('body',)
