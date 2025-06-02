from rest_framework import serializers
from .models import attendence 

class attendenceSerializers(serializers.ModelSerializer):
    class Meta :
        model = attendence
        fields =["employeeName", "date", "status"]
        