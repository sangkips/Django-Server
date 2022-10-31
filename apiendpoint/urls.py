from django.urls import path, include
from rest_framework import routers

from apiendpoint.models import Bio

from .views import django_models_json

router = routers.DefaultRouter()
router.register(r'bio', django_models_json, basename='bio')


urlpatterns = [
    path('', include(router.urls))
]