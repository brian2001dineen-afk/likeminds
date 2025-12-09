from . import views
from django.urls import path

urlpatterns = [
    path("", views.ClubList.as_view(), name='clubs'),
    path('create/', views.club_create, name='create'),
    path('<slug:slug>/', views.club_detail, name='club_detail'),
]
