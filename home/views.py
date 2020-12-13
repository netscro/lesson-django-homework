from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect, render
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
            return HttpResponseBadRequest('Некорректно заполнены данные в форме')


def student_update(request, id):  # noqa
    """
    This page updated information of students
    :param request:
    :param id: id of student in database
    :return: updated students info page
    """
    if request.method == 'GET':
        student = Student.objects.get(id=id)  # noqa
        one_student_form = StudentsAddForm(instance=student)

        context = {'form': one_student_form, 'student_id': student.id,
                   'student_name': student.name, 'student_surname': student.surname, }

        return render(request, 'student_update.html', context=context)

    elif request.method == 'POST':
        student = Student.objects.get(id=id)  # noqa
        one_student_form = StudentsAddForm(request.POST, instance=student)
        if one_student_form.is_valid():
            one_student_form.save()
            return redirect(reverse('students_info'))
        else:
            return HttpResponseBadRequest('Некорректно заполнены данные в форме')


def students_info(request):
    """
    This page print name all students in database
    :param request: output 'students-info.html'
    :return: name of all students
    """
    all_students = Student.objects.all()  # noqa

    if request.method == 'GET':
        students_add_form = StudentsAddForm()

        return render(request, 'students_info.html',
                      context={'all_students': all_students,
                               'form': students_add_form})

    elif request.method == 'POST':
        students_add_form = StudentsAddForm(request.POST)
        if students_add_form.is_valid():
            students_add_form.save()
            return redirect(reverse('students_info'))
        else:
            return HttpResponseBadRequest('Некорректно заполнены данные в форме')


def student_update_main(request): # noqa
    """
    Redirect /student-update/ page to /students-info/
    :param request: output 'students-info.html'
    :return: prints /students-info/ page
    """
    return redirect(reverse('students_info'))
