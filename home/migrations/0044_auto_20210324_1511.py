# Generated by Django 3.1.4 on 2021-03-24 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0043_student_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]