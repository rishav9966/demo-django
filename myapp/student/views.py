from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
# Create your views here.

def index(request):
    html = """<h1>This is the index of app name: student"""
    return HttpResponse(html)

def student_show(request):
    student = Student.objects.order_by('roll_no')
    # return render(request, '/student/student_show.html', {'student': student})
    return render(request, 'student/student_show.html', {'student': student})


