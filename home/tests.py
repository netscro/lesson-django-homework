from unittest import skip

from django.test import TestCase

# Create your tests here.
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from home.models import Student, Teacher


class StudentsApiTest(APITestCase):

    @skip
    def test_students_list_view(self):
        response = self.client.get(reverse('students_api-list'))
        base_response = {
            'count': 0,
            'next': None,
            'previous': None,
            'results': []
        }
        self.assertEqual(response.json(), base_response)

    @skip
    def test_student_create(self):
        Teacher.objects.create(name_surname='Ted')
        response = self.client.post(reverse('students_api-list'),
                                    {
                                        'name': 'One',
                                        'surname': 'student',
                                        'teacher': [1],
                                    })
        base_response = {
            'email': None,
            'is_active': False,
            'name': 'One',
            'surname': 'student',
            'teacher': [1],
        }

        self.assertEqual(response.json(), base_response)

    @skip
    def test_student_update(self):
        Teacher.objects.create(name_surname='Ted')
        Student.objects.create(name='One',
                               surname='Student',
                               )
        students = Student.objects.all()
        response = self.client.put(reverse('students_api-detail', kwargs={'pk': students[0].id}),
                                   {
                                        'name': 'Two',
                                        'surname': 'student',
                                        'teacher': [1],
                                   })
        base_response = {
            'email': None,
            'is_active': False,
            'name': 'Two',
            'surname': 'student',
            'teacher': [1],
        }

        self.assertEqual(response.json(), base_response)



