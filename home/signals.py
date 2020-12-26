import re

import gender_guesser.detector as gender
from django.db.models.signals import pre_delete, pre_save  # noqa
from django.dispatch import receiver

from home.models import Student


@receiver(pre_save, sender=Student)
def pre_save_normalized_name(sender, instance, **kwargs):  # noqa

    name_and_surname = f'{instance.name} {instance.surname}'
    instance.normalized_name = re.sub(r'[^\w\s]+|[\d]+|_', '',
                                      name_and_surname).lower()


@receiver(pre_save, sender=Student)
def pre_save_gender(sender, instance, **kwargs):  # noqa
    define_gender = gender.Detector()
    instance.sex = define_gender.get_gender(re.sub(r'[^\w\s]+|[\d]+|_',
                                                   '', instance.name).replace(' ', ''))  # noqa


@receiver(pre_delete, sender=Student)
def pre_delete_is_active(sender, instance, **kwargs):  # noqa
    instance.is_active = False
    instance.save()
    raise Exception('Student is not deleted')
