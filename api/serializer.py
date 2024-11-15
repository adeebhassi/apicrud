
from rest_framework import serializers
from .models import Company,Employee
import uuid
class EmployeeSerializer(serializers.Serializer):
    id=serializers.UUIDField(default=uuid.uuid4)
    name = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=255)
    email= serializers.CharField(max_length=100)

class CompanySerializer(serializers.ModelSerializer):
    employees =EmployeeSerializer(many=True)
    
    class Meta:
        model = Company
        fields = '__all__'
        
   