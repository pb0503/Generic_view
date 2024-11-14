from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from.serializers import EmployeeSerializer
from.models import Employee
# Create your views here.

class EmployeeApi(ListCreateAPIView):
    serializer_class=EmployeeSerializer
    queryset=Employee.objects.all()

class EmployeeDetails(RetrieveUpdateDestroyAPIView):
    serializer_class=EmployeeSerializer
    queryset=Employee.objects.all()