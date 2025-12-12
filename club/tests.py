from django.test import TestCase
from django.contrib.auth.models import User
from .models import Club
from .forms import ClubForm

# Create your tests here.

class ClubModelTest(TestCase):
    def test_club_creation_sets_slug(self):
        user = User.objects.create_user(username='testuser', password='pass')
        club = Club.objects.create(
            author=user,
            title="Test Club",
            excerpt="Short description",
            organizer_name="Test Organizer",
            organizer_email="test@example.com",
            personal_intro="Intro",
            club_briefing="Briefing",
            prerequisites="None",
            expectations="Be nice",
            schedule_description="Weekly",
            max_members=4,
            is_private=False,
            require_approval=True,
        )
        self.assertTrue(club.slug)
        self.assertEqual(len(club.slug), 8)

class ClubFormTest(TestCase):
    def test_club_form_valid(self):
        user = User.objects.create_user(username='testuser2', password='pass')
        form_data = {
            'author': user,
            'title': "Another Club",
            'excerpt': "Short description",
            'organizer_name': "Org Name",
            'organizer_email': "org@example.com",
            'personal_intro': "Intro",
            'club_briefing': "Briefing",
            'prerequisites': "None",
            'expectations': "Be active",
            'schedule_description': "Weekly",
            'max_members': 4,
            'is_private': False,
            'require_approval': True,
        }
        form = ClubForm(data=form_data)
        self.assertTrue(form.is_valid())
