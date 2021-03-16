from django.test import TestCase

# Create your tests here.
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from home.models import Student


class StudentsApiTest(APITestCase):

    def test_students_list_view(self):
        response = self.client.get(reverse('students_api-list'))
        empty_base_response = {
            'count': 0,
            'next': None,
            'previous': None,
            'results': []
        }
        self.assertEqual(response.json(), empty_base_response)

    def test_create_student_view(self):
        Student.objects.create(name='One', surname='student')
        response = self.client.get(reverse('students_api-list'))
        base_with_student = {
            'count': 1,
            'next': None,
            'previous': None,
            'results': [{'email': None,
                'is_active': True,
                'name': 'One',
                'surname': 'student',
                'teacher': []},
                ]
        }
        self.assertEqual(response.json(), base_with_student)

    def test_delete_student_view(self):
        Student.objects.create(name='One', surname='student')
        one_student = Student.objects.get(name='One')
        one_student.delete()
        response = self.client.get(reverse('students_api-list'))
        empty_base_response = {
            'count': 0,
            'next': None,
            'previous': None,
            'results': []
        }
        self.assertEqual(response.json(), empty_base_response)

    def test_student_update(self):
        Student.objects.create(name='One', surname='student')
        one_student = Student.objects.get(name='One')
        one_student.name = 'Two'
        one_student.save()
        response = self.client.get(reverse('students_api-list'))
        empty_base_response = {
            'count': 1,
            'next': None,
            'previous': None,
            'results': [{
                'email': None,
                'is_active': True,
                'name': 'Two',
                'surname': 'student',
                'teacher': []}]
        }
        self.assertEqual(response.json(), empty_base_response)

