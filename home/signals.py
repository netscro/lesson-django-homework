import re
import gender_guesser.detector as gender

from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver

from home.models import Student


@receiver(pre_save, sender=Student)
def pre_save_normalized_name(sender, instance, **kwargs):  # noqa

    name_and_surname = f'{instance.name} {instance.surname}'
    instance.normalized_name = re.sub('[^\w\s]|_', '', name_and_surname).lower()


@receiver(pre_save, sender=Student)
def pre_save_gender(sender, instance, **kwargs):  # noqa
    define_gender = gender.Detector()
    instance.sex = define_gender.get_gender(re.sub(r'[^\w\s]+|[\d]+',
                                                   '', instance.name).replace(' ', ''))

