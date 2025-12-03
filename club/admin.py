from django.contrib import admin

# Register your models here.
from .models import Club
from django_summernote.admin import SummernoteModelAdmin


# TODO: revise what decorators are
@admin.register(Club)
class ClubAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'description']
    list_filter = ('status', 'created_on',)
    # prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description',)

