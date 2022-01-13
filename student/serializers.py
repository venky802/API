from rest_framework import serializers
from .models import Student,Mark

class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model=Mark
        fields="__all__"
        

class StudentSerializer(serializers.ModelSerializer):
    id=MarkSerializer(read_only=True,many=True)
    class Meta:
        model=Student
        fields="__all__"
