# Generated by Django 3.1.4 on 2021-01-04 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20210104_1541'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportCard',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('report_card', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='report_card_marks',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.reportcard'),
        ),
    ]
