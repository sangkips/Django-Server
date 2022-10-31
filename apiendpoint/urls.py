from django.urls import path, include
from rest_framework import routers

from apiendpoint.models import Bio

from . import views


urlpatterns = [
    path('', views.home)
]