# Generated by Django 3.1.4 on 2021-03-16 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0029_auto_20210316_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='teacher',
            field=models.ManyToManyField(blank=True, to='home.Teacher'),
        ),
    ]
