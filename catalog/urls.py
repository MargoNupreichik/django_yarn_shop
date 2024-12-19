from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.view_catalog, name='view_catalog'),
]