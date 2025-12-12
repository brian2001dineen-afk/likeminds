from . import views
from django.urls import path

urlpatterns = [
    path("", views.ClubList.as_view(), name='clubs'),
    path('create/', views.club_create, name='create'),
    path('my-clubs/', views.my_clubs, name='my_clubs'),
    path('join/<slug:slug>/', views.club_join, name='club_join'),
    path('update/<slug:slug>/', views.club_update, name='club_update'),
    path('delete/<slug:slug>/', views.club_delete, name='club_delete'),
    path('<slug:slug>/', views.club_detail, name='club_detail'),
]
