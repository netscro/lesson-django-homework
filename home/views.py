from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect, render, get_object_or_404
# Create your views here.
from django.urls import reverse
from django.views import View

from home.forms import StudentForm
from home.models import Student


def home(request):  # noqa - # работает через функцию
    """
    This is page 'home/'
    :param request: output 'Hello world!'
    :return: Hello world
    """
    return HttpResponse('<h1>Hello world!</h1>')


class MainPage(View):
    """
    This is main page '/'
    #:param request: output 'Hello, this is a home page :)'
    #:return: Hello, this is a home page :)
    """

    def get(self, request): # noqa
        return render(request, 'index.html')


def students(request):  # работает через функцию
    """
    This page print information about all students in database
    :param request: output 'students.html'
    :return: information of all students
    """
    all_students = Student.objects.all()  # noqa

    if request.method == 'GET':
        students_add_form = StudentForm()

        return render(request, 'students.html',
                      context={'all_students': all_students,
                               'form': students_add_form})

    elif request.method == 'POST':
        students_add_form = StudentForm(request.POST)
        if students_add_form.is_valid():
            students_add_form.save()
            return redirect(reverse('students'))
        else:
            return HttpResponseBadRequest('Некорректно'
                                          ' заполнены данные в форме')


class StudentUpdateMain(View):
    """
    Redirect /student-update/ page to /students-info/
    #:param request: output 'students-info.html'
    #:return: prints /students-info/ page
    """

    def get(self, request): # noqa
        return redirect(reverse('students_info'))


class StudentUpdate(View):
    """
    This page updated information of students
    #:param request:
    #:param id: id of student in database
    :return: updated students info page
    """

    def get_student(self, id): # noqa
        return get_object_or_404(Student, id=id)

    def get(self, request, id): # noqa
        student = self.get_student(id)  # noqa
        student_form = StudentForm(instance=student)
        context = {'form': student_form, 'student': student}
        return render(request, 'student_update.html', context=context)

    def post(self, request, id): # noqa
        student = self.get_student(id)  # noqa
        student_form = StudentForm(request.POST, instance=student)
        if student_form.is_valid():
            student_form.save()
            return redirect(reverse('students_info'))
        else:
            return HttpResponseBadRequest('Некорректно '
                                          'заполнены данные в форме')


class StudentsInfo(View):
    """
    This page print name all students in database
    """

    def get(self, request): # noqa
        all_students = Student.objects.all()  # noqa
        students_add_form = StudentForm()

        return render(request, 'students_info.html',
                      context={'all_students': all_students,
                               'form': students_add_form})

    def post(self, request): # noqa
        students_add_form = StudentForm(request.POST)
        if students_add_form.is_valid():
            students_add_form.save()
            return redirect(reverse('students_info'))
        else:
            return HttpResponseBadRequest('Некорректно '
                                          'заполнены данные в форме')
