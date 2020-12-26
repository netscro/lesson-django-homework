from django.db import models

# Create your models here.


class Student(models.Model):
    """
    Students data fields in database
    """
    id = models.IntegerField(primary_key=True)  # noqa
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
