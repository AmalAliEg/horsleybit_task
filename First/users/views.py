from django.shortcuts import render
from django.http import HttpResponse
#import the models files from the same folder 
from .models import Course,Student,Grade, Teacher
# Create your views here.

def home(request):
    course=Course.objects.all()
    student= Student.objects.all()
    grade=Grade.objects.all()
    teacher= Teacher.objects.all()


    #pick each 
    return HttpResponse("hello, this is the users application")
