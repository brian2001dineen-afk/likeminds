from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Private"), (1, "Public"))

class Club(models.Model):
    """
    Stores a club created by a user :model:`auth.User`.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=8, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='clubs')
    excerpt = models.TextField(blank=False)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)
