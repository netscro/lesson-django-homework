from unittest import skip

from django.test import TestCase

# Create your tests here.
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from home.models import Student, Teacher, Subject, ReportCard


class StudentsApiTest(APITestCase):

    def setUp(self) -> None:
        Teacher.objects.create(name_surname='Ted')
        Student.objects.create(name='One',
                               surname='Student',)

    def test_students_list_view(self):
        response = self.client.get(reverse('students_api-list'))
        base_response = {
            'count': 1,
            'next': None,
            'previous': None,
            'results': [{
                'email': None,
                'is_active': True,
                'name': 'One',
                'surname': 'Student',
                'teacher': []
            }]
        }

        self.assertEqual(response.json(), base_response)

    def test_student_create(self):
        response = self.client.post(reverse('students_api-list'),
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

    def test_student_update(self):
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

    def test_student_delete(self):
        students = Student.objects.all()
        self.assertEqual(students.count(), 1)

        self.client.delete(reverse('students_api-detail', kwargs={'pk': students[0].id}))

        self.assertEqual(students.count(), 0)


class SubjectApiTest(APITestCase):

    def setUp(self) -> None:
        Subject.objects.create(title='Python')

    def test_subject_view(self):
        self.client.get(reverse('subject_api-list'))
        subjects = Subject.objects.all()
        self.assertEqual(subjects.count(), 1)

    def test_subject_create(self):
        response = self.client.post(reverse('subject_api-list'), {
            'title': 'Java',
        })

        base_response = {
            'id': 2,
            'title': 'Java',
        }
        self.assertEqual(response.json(), base_response)

    def test_subject_update(self):
        subjects = Subject.objects.all()
        response = self.client.put(reverse('subject_api-detail', kwargs={'pk': subjects[0].id}), {
            'title': 'JavaScript'
        })

        base_response = {
            'id': 1,
            'title': 'JavaScript',
        }
        self.assertEqual(response.json(), base_response)

    def test_subject_delete(self):
        subjects = Subject.objects.all()
        self.assertEqual(subjects.count(), 1)

        self.client.delete(reverse('subject_api-detail', kwargs={'pk': subjects[0].id}))

        self.assertEqual(subjects.count(), 0)


class ReportCardApiTest(APITestCase):

    def setUp(self) -> None:
        ReportCard.objects.create(report_card='zachetka')

    def test_report_card_view(self):
        self.client.get(reverse('report_card_api-list'))
        report_cards = ReportCard.objects.all()
        self.assertEqual(report_cards.count(), 1)

    def test_report_card_create(self):
        response = self.client.post(reverse('report_card_api-list'), {
            'report_card': 'zachetka_v_2_0',
        })

        print(response.json())

        base_response = {
            'id': 2,
            'report_card': 'zachetka_v_2_0',
        }
        self.assertEqual(response.json(), base_response)

    def test_report_cart_update(self):
        report_cards = ReportCard.objects.all()
        response = self.client.put(reverse('report_card_api-detail', kwargs={'pk': report_cards[0].id}), {
            'report_card': 'zachetka_v_2_0'
        })

        base_response = {
            'id': 1,
            'report_card': 'zachetka_v_2_0',
        }
        self.assertEqual(response.json(), base_response)

    def test_report_card_delete(self):
        report_cards = ReportCard.objects.all()
        self.assertEqual(report_cards.count(), 1)

        self.client.delete(reverse('report_card_api-detail', kwargs={'pk': report_cards[0].id}))
        self.assertEqual(report_cards.count(), 0)
