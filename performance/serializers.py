from rest_framework import serializers
from .models import performance 

class performance_serializer(serializers.ModelSerializer):
    class Meta:
        model= performance
        fields=['employee','rating','reviewDate']