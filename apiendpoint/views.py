from django.shortcuts import render
from rest_framework import status, viewsets
from .serializers import BioSerializer
from .models import Bio
from django.http import HttpResponse
import json


# Create your views here.
class BioViewSet(viewsets.ModelViewSet):
    queryset = Bio.objects.all()
    serializer_class = BioSerializer


    def post(self, request, **kwargs):
        response_data = super().list(request)
        return HttpResponse(json.dumps(response_data),content_type="application/json")