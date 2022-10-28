from django.urls import path, include
from rest_framework import routers
from . import views

from .views import BioViewSet

router = routers.DefaultRouter()
router.register(r'bio', BioViewSet)


urlpatterns = [
    path('', include(router.urls))
]