'''
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

'''
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Bio

def django_models_json(request):
    obj = Bio.objects.first()
    data = serialize("json", fields=('slackUsername', 'backend', 'age', 'bio'))
    return HttpResponse(data, content_type="application/json")