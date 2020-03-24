from rest_framework import serializers
from . models import  employee

class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        Model = employee
        fields='__all__'