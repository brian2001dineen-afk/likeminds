import random
import string

from django.contrib.auth.models import User
from django.db import models

def random_slug(length=8):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))


class Club(models.Model):
    """
    Stores a club created by a user :model:`auth.User`.
    """
    # Logic fields
    slug = models.SlugField(unique=True, blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='clubs')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    unapproved_members = models.ManyToManyField(
        User, related_name='waitlist', blank=True)
    approved_members = models.ManyToManyField(
        User, related_name='club_members', blank=True)

    # Form fields
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=300)
    organizer_name = models.CharField(max_length=100)
    organizer_email = models.EmailField()
    personal_intro = models.TextField()
    club_briefing = models.TextField()
    prerequisites = models.TextField()
    expectations = models.TextField()
    schedule_description = models.TextField()
    max_members = models.PositiveIntegerField(default=4)
    is_private = models.BooleanField(default=False)
    require_approval = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = random_slug()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | created by {self.author}"
