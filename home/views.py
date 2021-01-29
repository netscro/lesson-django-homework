import csv
import uuid

from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView

from home.emails import send_email
from home.forms import ReportCardForm, StudentFilter, StudentForm
from home.models import ReportCard, Student


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

    def get(self, request):  # noqa
        return render(request, 'index.html')


# ----------------------------------------------------------------------
# def students(request):  # работает через функцию
#     """
#     This page print information about all students in database
#     :param request: output 'students.html'
#     :return: information of all students
#     """
#     all_students = Student.objects.all()  # noqa
#
#     if request.method == 'GET':
#         students_add_form = StudentForm()
#
#         return render(request, 'students.html',
#                       context={'all_students': all_students,
#                                'form': students_add_form})
#
#     elif request.method == 'POST':
#         students_add_form = StudentForm(request.POST)
#         if students_add_form.is_valid():
#             students_add_form.save()
#             return redirect(reverse('students'))
#         else:
#             return HttpResponseBadRequest('Некорректно'
#                                           ' заполнены данные в форме')
# -----------------------------------------------------------------------


class Students(CreateView):
    """
    This page create new student in database
    """
    model = Student
    fields = ['name', 'surname', 'age',
              'social_url', 'email',
              'description', 'subject', 'teacher']
    template_name = 'students.html'
    success_url = reverse_lazy('students_info')

    def form_valid(self, form):
        report_card = ReportCard()
        report_card.report_card = uuid.uuid4()
        report_card.save()
        form.instance.report_card = report_card
        return super(Students, self).form_valid(form)


class StudentUpdateMain(View):
    """
    Redirect /student-update/ page to /students-info/
    #:param request: output 'students-info.html'
    #:return: prints /students-info/ page
    """

    def get(self, request):  # noqa
        return redirect(reverse('students_info'))


# ----------------------------------------------------------------------------
# class StudentUpdate(View):
#     """
#     This page updated information of students
#     #:param request:
#     #:param id: id of student in database
#     :return: updated students info page
#     """
#
#     def get_student(self, id):  # noqa - A002 argument "id" is shadowing a python builtin
#         return get_object_or_404(Student, id=id)
#
#     def get(self, request, id):  # noqa - A002 argument "id" is shadowing a python builtin
#         student = self.get_student(id)  # noqa - A002 argument "id" is shadowing a python builtin
#         student_form = StudentForm(instance=student)
#         context = {'form': student_form, 'student': student}
#         return render(request, 'student_update.html', context=context)
#
#     def post(self, request, id):  # noqa - A002 argument "id" is shadowing a python builtin
#         student = self.get_student(id)  # noqa - A002 argument "id" is shadowing a python builtin
#         student_form = StudentForm(request.POST, instance=student)
#         if student_form.is_valid():
#             student_form.save()
#             return redirect(reverse('students_info'))
#         else:
#             return HttpResponseBadRequest('Некорректно '
#                                           'заполнены данные в форме')
# ----------------------------------------------------------------------------


class StudentUpdate(UpdateView):
    """
    This page updated information of students
    """
    model = Student
    fields = ['name', 'surname', 'age',
              'social_url', 'email',
              'description', 'subject', 'teacher']
    template_name = 'student_update.html'
    success_url = reverse_lazy('students_info')


# ----------------------------------------------------------------------------
# оставил для себя чтоб не забыть как работает через View
#
# class StudentsInfo(View):
#     """
#     This page print name all students in database
#     """
#
#     def get(self, request):  # noqa
#         all_students = Student.objects.all()  # noqa
#         students_add_form = StudentForm()
#
#         filter_student = StudentFilter(request.GET, queryset=all_students)
#
#         return render(request, 'students_info.html',
#                       context={'all_students': all_students,
#                                'form': students_add_form,
#                                'filter': filter_student})
#
#     def post(self, request):  # noqa
#         students_add_form = StudentForm(request.POST)
#         if students_add_form.is_valid():
#             students_add_form.save()
#             return redirect(reverse('students_info'))
#         else:
#             return HttpResponseBadRequest('Некорректно '
#                                           'заполнены данные в форме')
# ---------------------------------------------------------------------------


class StudentsInfo(ListView):
    """
    This page print name all students in database
    """

    model = Student
    template_name = 'students_info.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = StudentFilter(self.request.GET, queryset=Student.objects.all())
        return context


class ReportCardInfo(View):
    """
    This page updated information of report card of each student
    #:param request:
    #:param id: id of report card in database
    :return: updated students info page
    """

    def get(self, request):
        all_students = Student.objects.all()  # noqa
        return render(request, 'report_card_info.html',
                      context={'all_students': all_students})


class ReportCardDelete(View):
    """
    This page delete report card of a student with POST request
    """

    def get_report_card_id(self, id):  # noqa -  A002 argument "id" is shadowing a python builtin
        return get_object_or_404(ReportCard, id=id)

    def get(self, request, id):  # noqa - A002 argument "id" is shadowing a python builtin
        report_card = self.get_report_card_id(id)
        report_card_form = ReportCardForm(instance=report_card)
        context = {'form': report_card_form, 'report_card': report_card}
        return render(request, 'report_card_delete.html', context=context)

    def post(self, request, id):  # noqa - A002 argument "id" is shadowing a python builtin
        report_card = self.get_report_card_id(id)
        report_card_form = ReportCardForm(request.POST, instance=report_card)
        report_card.delete()
        return redirect(reverse('report_card_info'),
                        report_card_form=report_card_form)


class SubjectInfo(View):
    """
    This page updated information of teacher of each student
    """

    def get(self, request):
        all_students = Student.objects.all()  # noqa
        students_add_form = StudentForm()
        return render(request, 'subject_info.html',
                      context={'all_students': all_students,
                               'form': students_add_form})

    def post(self, request):  # noqa
        students_add_form = StudentForm(request.POST)
        if students_add_form.is_valid():
            student = students_add_form.save()

            student_marks = ReportCard()
            student_marks.report_card = uuid.uuid4()
            student_marks.save()

            student.report_card = student_marks
            student.save()

            return redirect(reverse('subject_info'))
        else:
            return HttpResponseBadRequest('Некорректно '
                                          'заполнены данные в форме')


class SubjectDelete(View):
    """
    This page delete a student of subject
    """

    def get_student(self, id):  # noqa -  A002 argument "id" is shadowing a python builtin
        return get_object_or_404(Student, id=id)

    def get(self, request, id):  # noqa -  A002 argument "id" is shadowing a python builtin
        all_students = Student.objects.all()  # noqa
        students_add_form = StudentForm()
        student = self.get_student(id)  # noqa -  A002 argument "id" is shadowing a python builtin

        students_add_form_update = StudentForm(instance=student)

        context = {'student': student, 'form': students_add_form,
                   'form_save': students_add_form_update}
        return render(request, 'subject_delete.html', context=context)

    def post(self, request, id):  # noqa -  A002 argument "id" is shadowing a python builtin
        student = self.get_student(id)  # noqa -  A002 argument "id" is shadowing a python builtin
        student.delete()

        return redirect(reverse('subject_info'))


class SubjectUpdate(View):
    """
    This page updated information of students
    #:param request:
    #:param id: id of student in database
    :return: updated students info page
    """

    def post(self, request, id):  # noqa - A002 argument "id" is shadowing a python builtin
        student = get_object_or_404(Student, id=id)  # noqa - A002 argument "id" is shadowing a python builtin
        student_form = StudentForm(request.POST, instance=student)
        if student_form.is_valid():
            student_form.save()
            return redirect(reverse('subject_info'))
        else:
            return HttpResponseBadRequest('Некорректно '
                                          'заполнены данные в форме')


class TeacherInfo(View):
    """
    This page view information of teacher of each student
    """

    def get(self, request):
        students_add_form = StudentForm()
        all_students = Student.objects.all()  # noqa
        return render(request, 'teacher_info.html',
                      context={'all_students': all_students,
                               'form': students_add_form})

    def post(self, request):  # noqa
        students_add_form = StudentForm(request.POST)
        if students_add_form.is_valid():
            student = students_add_form.save()

            student_marks = ReportCard()
            student_marks.report_card = uuid.uuid4()
            student_marks.save()

            student.report_card = student_marks
            student.save()

            return redirect(reverse('teacher_info'))
        else:
            return HttpResponseBadRequest('Некорректно '
                                          'заполнены данные в форме')


class TeacherDelete(View):
    """
    This page delete a student of subject
    """

    def get_student(self, id):  # noqa -  A002 argument "id" is shadowing a python builtin
        return get_object_or_404(Student, id=id)

    def get(self, request, id):  # noqa -  A002 argument "id" is shadowing a python builtin
        all_students = Student.objects.all()  # noqa
        students_add_form = StudentForm()
        student = self.get_student(id)  # noqa -  A002 argument "id" is shadowing a python builtin

        students_add_form_update = StudentForm(instance=student)

        context = {'student': student, 'form': students_add_form,
                   'form_save': students_add_form_update}
        return render(request, 'teacher_delete.html', context=context)

    def post(self, request, id):  # noqa -  A002 argument "id" is shadowing a python builtin
        student = self.get_student(id)  # noqa -  A002 argument "id" is shadowing a python builtin
        student.delete()

        return redirect(reverse('teacher_info'))


class TeacherUpdate(View):
    """
    This page updated information of students
    #:param request:
    #:param id: id of student in database
    :return: updated students info page
    """

    def post(self, request, id):  # noqa - A002 argument "id" is shadowing a python builtin
        student = get_object_or_404(Student, id=id)  # noqa - A002 argument "id" is shadowing a python builtin
        student_form = StudentForm(request.POST, instance=student)
        if student_form.is_valid():
            student_form.save()
            return redirect(reverse('teacher_info'))
        else:
            return HttpResponseBadRequest('Некорректно '
                                          'заполнены данные в форме')


class JsonStudentsView(View):

    def get(self, request):
        all_students = Student.objects.all()
        json_students = []
        for one_student in all_students:
            dict_one_student = {"id": f"{one_student.id}",
                                "name": f"{one_student.name}",
                                "second_name": f"{one_student.surname}",
                                "age": f"{one_student.age}"}
            json_students.append(dict_one_student)

        return JsonResponse({"students": json_students})

        # return JsonResponse({"students": model_to_dict(Student.objects.first())}) # noqa - E501 line too long
        # --> делает тоже самое только без цикла для одного/первого студента
        # (*пометка для меня чтоб запомнить)

        # return JsonResponse({"students": list(all_students.values())})
        # --> выводит всю информацию о студенте, без цикла для всех студентов
        # (*пометка для меня чтоб запомнить)


class CSVView(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = "attachment; " \
                                          "filename=students_data.csv"
        write_csv = csv.writer(response)
        write_csv.writerow(['Name', 'Surname', 'Age', 'Sex'])

        students = Student.objects.all()
        for one_student in students:
            write_csv.writerow([one_student.name, one_student.surname,
                                one_student.age, one_student.sex])
        return response


class SendEmail(View):

    def get(self, request):
        send_email(subject='Письмо счастья :)',
                   message='Вам сказачно повезло, вы выиграли бочку виски!',
                   recipient_list=['kovalev_evgeniy@list.ru'])
        return HttpResponse('Письмо отправлено!')
