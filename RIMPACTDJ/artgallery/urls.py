from django.contrib import admin
from django.urls import path, include
from artgallery import views
from .views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('index',views.index, name='index'),
    path('tinymce/', include('tinymce.urls')),
    path('gallery', views.artgallery, name='artgallery'),
    path('post/<slug:url>',post),
    path('techteam', views.techteam, name='techteam'),
    path('performances', views.performance, name='performances'),
]