# Generated by Django 3.1.4 on 2021-03-03 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_auto_20210119_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='picture',
            field=models.ImageField(null=True, upload_to='pictures'),
        ),
    ]
