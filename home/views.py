from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from home.models import Student


def home(request):  # noqa
    """
    This is page 'home/'
    :param request: output 'Hello world!'
    :return: Hello world
    """
    return HttpResponse('<h1>Hello world!</h1>')


def main_page(request):
    """
    This is main page '/'
    :param request: output 'Hello, this is a home page :)'
    :return: Hello, this is a home page :)
    """
    return render(request, 'index.html')


def students(request):
    """
    This page print information about all students in database
    :param request: output 'students.html'
    :return: information of all students
    """
    student_data = Student()  # noqa
    all_students = Student.objects.all()
    return render(request, 'students.html',
                  context={'all_students': all_students})
