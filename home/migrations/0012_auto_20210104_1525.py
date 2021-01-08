# Generated by Django 3.1.4 on 2021-01-04 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20210104_1356'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='teacher_name_surname',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.teacher'),
        ),
    ]
