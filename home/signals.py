import re

from django.db.models.signals import pre_save
from django.dispatch import receiver

from home.models import Student


@receiver(pre_save, sender=Student)
def pre_save_normalized_name(sender, instance, **kwargs):  # noqa

    name_and_surname = f'{instance.name} {instance.surname}'
    instance.normalized_name = re.sub('[^\w\s]|_', '', name_and_surname).lower()

# также чтобы сигналы начали работать нужно сделать их импорт в apps.py
# и указать default_app_config в __init__.py приложения
