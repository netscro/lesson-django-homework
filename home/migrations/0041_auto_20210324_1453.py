# Generated by Django 3.1.4 on 2021-03-24 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0040_student_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='student',
            name='updated_at',
        ),
    ]
