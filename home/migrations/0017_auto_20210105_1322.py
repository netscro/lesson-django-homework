# Generated by Django 3.1.4 on 2021-01-05 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20210104_1729'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='report_card_marks',
            new_name='report_card',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='subject_title',
            new_name='subject',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='teacher_name_surname',
            new_name='teacher',
        ),
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='subject',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
