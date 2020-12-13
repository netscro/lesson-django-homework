from django.forms import ModelForm

from home.models import Student


class StudentsAddForm(ModelForm):

    class Meta:
        model = Student
        fields = ['name', 'surname', 'age', 'description', 'social_url']
