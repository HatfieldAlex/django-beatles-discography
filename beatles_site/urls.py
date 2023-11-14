from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:album_name_slug>', views.album_detail, name='album_detail'),
    path('please_please_me', views.please_please_me, name='please_please_me'),
    path('help', views.help, name='help'),
    path('let_it_be', views.let_it_be, name='let_it_be')
]