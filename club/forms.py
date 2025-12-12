from .models import Club
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Field, Div


class ClubForm(forms.ModelForm):
    """
    Creates a club form for creating and updating club instances.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Crispy helper configured for Bootstrap5 inside modal
        self.helper = FormHelper()
        self.helper.form_tag = False  # prevent nested <form> in modal
        self.helper.disable_csrf = True
        self.helper.layout = Layout(
            Field('title'),
            Field('excerpt'),
            Div(
                Row(
                    Column(Field('organizer_name'), css_class='col-md-6'),
                    Column(Field('organizer_email'), css_class='col-md-6'),
                ),
                css_class='mb-3'
            ),
            Field('personal_intro'),
            Field('club_briefing'),
            Row(
                Column(Field('prerequisites'), css_class='col-md-6'),
                Column(Field('expectations'), css_class='col-md-6'),
            ),
            Row(
                Column(Field('schedule_description'), css_class='col-md-8'),
                Column(Field('max_members'), css_class='col-md-4'),
            ),
            Row(
                Column(Field('is_private'), css_class='col-md-6'),
                Column(Field('require_approval'), css_class='col-md-6'),
            ),
        )

    class Meta:
        model = Club
        fields = [
            'title',
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
        # Map HTML display widgets to model fields
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "e.g., Quantum Mechanics Study Group",
                'required': 'required',
                'id': 'clubName',
            }),
            'excerpt': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Briefly describe what you'll be studying, your goals, and what participants can expect (max 300 characters)...",
                'rows': 4,
                'required': 'required',
                'id': 'clubExcerpt',
            }),
            'organizer_name': forms.TextInput(attrs={
                'class': 'form-control',
                'required': 'required',
                'id': 'organizerName',
            }),
            'organizer_email': forms.EmailInput(attrs={
                'class': 'form-control',
                'required': 'required',
                'id': 'organizerEmail',
            }),
            'personal_intro': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Write a little about your background and motivations for starting this club...",
                'rows': 4,
                'required': 'required',
                'id': 'personalIntro',
            }),
            'club_briefing': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Write a detailed abstract about your subject choice, including material references, and anything else a potential member will need to get an idea of what the club is about...",
                'rows': 14,
                'required': 'required',
                'id': 'clubBriefing',
            }),
            'prerequisites': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': "List any required background knowledge, previous courses, or experience...",
                'rows': 3,
                'required': 'required',
                'id': 'prerequisites',
            }),
            'expectations': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Describe participation requirements, reading commitments, attendance expectations...",
                'rows': 3,
                'required': 'required',
                'id': 'expectations',
            }),
            'schedule_description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Describe how you will meet each week, e.g. Zoom, Teams or otherwise. Bullet point a proposed schedule for when you will meet. This can be left blank and changed later to suit member needs, but it's recommended to give some context for how you plan to schedule meetings...",
                'rows': 6,
                'required': 'required',
                'id': 'scheduleDescription',
            }),
            'max_members': forms.Select(
                choices=[(i, str(i)) for i in range(2, 9)],
                attrs={'class': 'form-select', 'id': 'maxMembers'
                       }),
            'is_private': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'id': 'clubVisibility',
            }),
            'require_approval': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'id': 'requireApproval',
            }),
        }
