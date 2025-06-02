from django.shortcuts import render
from rest_framework import generics
from .models import attendence 
from .serializers import attendenceSerializers
# Create your views here.


class attendenceListCreate(generics.ListCreateAPIView): 
    queryset= attendence.objects.all()
    serializer_class= attendenceSerializers