from django.shortcuts import render
from app1.models import Student

# Create your views here.

def Home(request):
    stud=Student.objects.all()
    return render(request, 'home.html', {'stu':stud})

def About(request):
    return render(request, 'about.html',)


