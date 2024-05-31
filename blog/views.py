from django.shortcuts import render
from .models import Category, EmployeeAbout
from .serializers import EmployeeAboutSerializer
from rest_framework import viewsets


class ProductsViews(viewsets.ModelViewSet):
    queryset = EmployeeAbout.objects.all().order_by('-id')
    serializer_class = EmployeeAboutSerializer
    lookup_field = 'id'

