from django.shortcuts import render
from rest_framework import status, viewsets
from .serializers import BioSerializer
from .models import Bio
from rest_framework.response import Response


# Create your views here.
class BioViewSet(viewsets.ModelViewSet):
    queryset = Bio.objects.all()
    serializer_class = BioSerializer


    def list(self, request):
        response = super().list(request)
        return Response({"data": response.data})