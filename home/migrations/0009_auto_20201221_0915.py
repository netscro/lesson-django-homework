# Generated by Django 3.1.4 on 2020-12-21 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20201221_0757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='social_url',
            field=models.URLField(blank=True, max_length=300, null=True),
        ),
    ]