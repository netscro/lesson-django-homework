import re
import uuid

import gender_guesser.detector as gender
from django.db.models.signals import pre_delete, pre_save  # noqa
from django.dispatch import receiver

from home.models import Student, ReportCard


@receiver(pre_save, sender=Student)
def pre_save_normalized_name(sender, instance, **kwargs):  # noqa

    name_and_surname = f'{instance.name} {instance.surname}'
    instance.normalized_name = re.sub(r'[^\w\s]+|[\d]+|_', '',
                                      name_and_surname).lower()
    if not instance.report_card:
        report_card = ReportCard()
        report_card.report_card = uuid.uuid4()
        report_card.save()
        instance.report_card = report_card


@receiver(pre_save, sender=Student)
def pre_save_gender(sender, instance, **kwargs):  # noqa
    define_gender = gender.Detector()
    instance.sex = define_gender.get_gender(re.sub(r'[^\w\s]+|[\d]+|_',
                                                   '', instance.name).replace(' ', ''))  # noqa


# @receiver(pre_delete, sender=Student)
# def pre_delete_is_active(sender, instance, **kwargs):  # noqa
#     report_card = ReportCard.objects.get(pk=instance.report_card.id)
#     report_card.delete()
