from django.contrib import admin

from .models import Student,Mark
from .import views
from django.urls import path,include
from rest_framework.routers import DefaultRouter




 

    
router = DefaultRouter()
router.register("Student",views.studentapi)
router.register("Mark",views.marksapi)
urlpatterns = router.urls