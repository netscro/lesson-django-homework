from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Student(models.Model):
    """
    Students data fields in database
    """
    id = models.AutoField(primary_key=True) # noqa - A003
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=200)
    age = models.IntegerField(null=True)
    sex = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    birthday = models.DateField(null=True)
    email = models.EmailField(max_length=200, null=True)
    social_url = models.URLField(max_length=300, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    normalized_name = models.CharField(max_length=300, null=True, blank=True)
    subject = models.ForeignKey('home.Subject',
                                on_delete=models.SET_NULL, null=True)
    teacher = models.ManyToManyField('home.Teacher')
    picture = models.ImageField(upload_to='pictures', null=True, blank=True)
    report_card = models.OneToOneField('home.ReportCard',
                                       on_delete=models.CASCADE,
                                       null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


class Subject(models.Model):
    """
    Information about the subject which students study
    one to many
    """
    id = models.AutoField(primary_key=True) # noqa - A003
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title


class Teacher(models.Model):
    """
    Information about the teacher which study a students
    one to many
    """
    id = models.AutoField(primary_key=True) # noqa - A003
    name_surname = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name_surname


class ReportCard(models.Model):
    """
    Information about the report card of a students
    one to one
    """
    id = models.AutoField(primary_key=True) # noqa - A003
    report_card = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.report_card


class Currency(models.Model):
    id = models.AutoField(primary_key=True) # noqa - A003
    ccy = models.CharField(max_length=100)
    base_ccy = models.CharField(max_length=100)
    buy = models.CharField(max_length=100, null=True,)
    sale = models.CharField(max_length=100, null=True,)
    date = models.CharField(max_length=100, null=True,)


class UserSignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
