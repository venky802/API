from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Student(models.Model):
    rollno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=60)
    dob = models.DateTimeField()

class Mark(models.Model):
    rollno=models.ForeignKey(Student,related_name="id",on_delete=CASCADE)
    marks=models.IntegerField()
    grade=models.CharField(max_length=1)
    