from django.shortcuts import render

# Create your views here.
from .models import Teacher,Course,Student

def index(request):
    return render(request, 'index.html')

def teachers(request):
    teachers = Teacher.objects.all()
    return render(request,'teachers.html',{'teachers':teachers})

def courses(request):
    courses = Course.objects.all()
    return render(request,'courses.html',{'courses':courses})

def students(request):
    students = Student.objects.all()
    return render(request,'students.html',{'students':students})

