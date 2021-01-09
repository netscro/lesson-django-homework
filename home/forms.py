from django.forms import ModelForm

from home.models import Student, ReportCard, Subject


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
