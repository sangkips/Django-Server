from . models import  Bio
from rest_framework import serializers

class BioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bio
        fields = 'slackUsername', 'backend', 'age', 'bio'