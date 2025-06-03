from django.shortcuts import render
from rest_framework import generics
from .models import performance
from .serializers import performance_serializer
# Create your views here.

class performanceListCreate(generics.ListCreateAPIView):
    queryset= performance.objects.all()
    serializer_class= performance_serializer
