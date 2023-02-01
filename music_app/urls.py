from django.urls import path

from music_app import views

urlpatterns =[
    path('', views.music_app, name='music_app')
]