from django.forms import ModelForm

from home.models import Student, ReportCard


class StudentForm(ModelForm):

    class Meta:
        model = Student
        fields = ['name', 'surname', 'age',
                  'social_url', 'email', 'description']


class ReportCardForm(ModelForm):

    class Meta:
        model = ReportCard
        fields = ['report_card']
