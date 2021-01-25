from abc import ABC

from django.core.management import BaseCommand

from home.models import Student


class Command(BaseCommand):

    def add_arguments(self, parser):
        """
        The number of default students added to the database
        """
        parser.add_argument('-l', '--len', type=int, default=10)

    def handle(self, *args, **options):
        """
        In a loop, prints the specified
        number of students in func "add_arguments"
        """
        # ниже вставлять код для тестиорования



