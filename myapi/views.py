from django.shortcuts import render;

# Create your views here.
# views.py
from rest_framework import viewsets

from .serializers import HeroSerializer, EmployeeSerializer
from .models import Hero, Employee


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('name')
    serializer_class = EmployeeSerializer



