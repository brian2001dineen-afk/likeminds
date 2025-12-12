from django.contrib import admin
from .models import Club 
# Register your models here.

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'max_members', 'is_private', 'require_approval')
    search_fields = ('title', 'author__username')
    list_filter = ('is_private', 'require_approval')
