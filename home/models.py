from django.db import models

# Create your models here.


class Student(models.Model):
    """
    Student data of all students in database
    """
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=200)
