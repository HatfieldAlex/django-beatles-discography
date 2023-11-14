from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:album_name_slug>', views.album_detail, name='album_detail'),
    path('<slug:album_name_slug>/tracks', views.album_tracks, name='album_tracks'),
]