from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.news_feed, name='news_feed'),
]
