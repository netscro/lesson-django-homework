from django.core.management import BaseCommand
from faker import Faker  # noqa

from home.models import Student, Subject


class Command(BaseCommand):

    help = 'Add new student in to the database'  # noqa

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
        faker = Faker()

        for new_student in range(options['len']):
            subject, _ = Subject.objects.get_or_create(title='Python')
            subject.save()

            student = Student()
            student.name = faker.first_name()
            student.surname = faker.last_name()
            student.age = faker.random_int(min=18, max=50)
            # student.sex = faker.simple_profile()['sex']
            student.address = faker.address()
            student.description = faker.text()
            student.birthday = faker.date_between()
            student.email = faker.email()
            student.social_url = f'http://{faker.domain_name()}'
            student.is_active = faker.boolean(chance_of_getting_true=100)

            student.subject = subject

            student.save()
