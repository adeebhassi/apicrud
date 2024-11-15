from djongo import models
import uuid
# Create your models here.
class Employee(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    address=models.CharField(max_length=200)
        
    def __str__(self) -> str:
        return self.name

class Company(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    location=models.CharField(max_length=100)
    employees=models.ArrayField(model_container=Employee)
    
    def __str__(self) -> str:
        return self.name
    