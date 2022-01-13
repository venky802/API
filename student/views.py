from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse
from .models import Student,Mark
from .serializers import StudentSerializer,MarkSerializer
from rest_framework import serializers, viewsets
# Create your views here.

class studentapi(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer




class marksapi(viewsets.ModelViewSet):
    queryset=Mark.objects.all()
    serializer_class=MarkSerializer

