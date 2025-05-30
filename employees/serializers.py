#serializers take an instance of a python object
#returns something that we can interact with 
# from our API 
from rest_framework import serializers
from .models import employees
from .models import department

class employee_serializer(serializers.ModelSerializer):
    class Meta:
        model = employees
        fields =["name", "email","phoneNumber","address","dateOfJoining", "department"]

class department_serializer(serializers.ModelSerializer):
    class Meta: 
        model = department
        fields=["department"]