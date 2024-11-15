# apiss/views.py

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Company,Employee
from .serializer import CompanySerializer

@api_view(['POST','GET'])
def submit_company_data(request):
    if request.method == 'POST':
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
@api_view(['PUT','GOT','DELETE'])  
def company_data(request,id):
    if request.method=='DELETE':
        print(id)
        company = Company.objects.get(id=id)
        company.delete()
        return Response()
