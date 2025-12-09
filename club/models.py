import random
import string

from django.contrib.auth.models import User
from django.db import models

STATUS = ((0, "Private"), (1, "Public"))

def random_slug(length=8):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))


class Club(models.Model):
    """
    Stores a club created by a user :model:`auth.User`.
    """
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    # tags = models.
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='clubs')
    excerpt = models.TextField(blank=False)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)
    unapproved_members = models.ManyToManyField(
        User, related_name='waitlist', blank=True)
    approved_members = models.ManyToManyField(
        User, related_name='club_members', blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = random_slug()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | created by {self.author}"
