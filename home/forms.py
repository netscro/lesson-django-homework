from django.forms import ModelForm

import django_filters

from home.models import ReportCard, Student, Subject


class StudentForm(ModelForm):

    class Meta:
        model = Student
        fields = ['name', 'surname', 'age',
                  'social_url', 'email', 'description', 'subject', 'teacher']


class ReportCardForm(ModelForm):

    class Meta:
        model = ReportCard
        fields = ['report_card']


class SubjectInfoForm(ModelForm):

    class Meta:
        model = Subject
        fields = ['title']


class StudentFilter(django_filters.FilterSet):
    # name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Student
        fields = ['subject', 'teacher', 'report_card']
