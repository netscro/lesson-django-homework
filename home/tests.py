
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





