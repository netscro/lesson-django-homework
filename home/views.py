from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from home.forms import StudentsAddForm
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
    all_students = Student.objects.all()  # noqa

    if request.method == 'GET':
        students_add_form = StudentsAddForm()

        return render(request, 'students.html',
                      context={'all_students': all_students,
                               'form': students_add_form})

    elif request.method == 'POST':
        students_add_form = StudentsAddForm(request.POST)
        if students_add_form.is_valid():
            students_add_form.save()
            return redirect(reverse('students'))
        else:
            return HttpResponseBadRequest('Некорректно заполнены в форме')
