from django.urls import path
from . import views

urlpatterns = [
    path('welcome/', views.welcome, name="home"),
    path('tweet_detail/<int: pk>/', views.tweet_details, name="tweet_details"),
]