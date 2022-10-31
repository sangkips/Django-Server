from django.urls import path, include
from rest_framework import routers
from . import views

from .views import django_models_json

router = routers.DefaultRouter()
router.register(r'bio', django_models_json)


urlpatterns = [
    path('', include(router.urls))
]