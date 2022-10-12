from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .models import Departments,Employees
from .serializers import DepartmentSerializer,EmployeeSerializer  
from rest_framework.decorators import api_view,permission_classes  
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class PostMetod(GenericAPIView): 
    serializer_class = DepartmentSerializer
    queryset = Departments.objects.all()
    permission_classes = (IsAuthenticated,)
    def post(self,request):
        department_data=request.data
        departments_serializer=DepartmentSerializer(data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return Response("Added Successfully")
        return Response("Failed to Add")

class PutMetod(GenericAPIView): 
    serializer_class = DepartmentSerializer
    queryset = Departments.objects.all()
    permission_classes = (IsAuthenticated,)
    def put(self,request,id = 0):
        department_data=request.data
        department=Departments.objects.get(DepartmentId=id)
        departments_serializer=DepartmentSerializer(department,data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return Response("Updated Successfully")
        return Response("Failed to Update")
 
class DepartmentClass(GenericAPIView):   

    serializer_class = DepartmentSerializer
    queryset = Departments.objects.all()  
    @permission_classes([IsAuthenticated])

    @api_view(['GET'])  
    def GetDepartment(self): 
        departments = Departments.objects.all()
        departments_serializer=DepartmentSerializer(departments,many=True)
        return Response(departments_serializer.data)  
 
    @api_view(['GET']) 
    def GetDepartmentByID(self,id=0):
        department=Departments.objects.get(DepartmentId=id)
        departments_serializer=DepartmentSerializer(department)
        return Response(departments_serializer.data)
 
    @api_view(['DELETE'])    
    def DeleteDepartment(self,id=0):
        department=Departments.objects.get(DepartmentId=id)
        department.delete()
        return Response("Deleted Successfully")    
