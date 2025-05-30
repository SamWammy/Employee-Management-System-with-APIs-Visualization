from django.shortcuts import render
from rest_framework import generics
from .models import employees
from .models import department
from .serializers import employee_serializer
from .serializers import department_serializer

class employeeListCreate(generics.ListCreateAPIView):
    queryset= employees.objects.all()
    serializer_class= employee_serializer


class departmentListCreate(generics.ListCreateAPIView):
    queryset=department.objects.all()
    serializer_class = department_serializer