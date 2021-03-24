
# Create your tests here.

import freezegun
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from home.models import ReportCard, Student, Subject, Teacher


@freezegun.freeze_time('1987-06-07 00:00:00')
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
                'created_at': '1987-06-07T00:00:00',
                'email': None,
                'is_active': True,
                'name': 'One',
                'surname': 'Student',
                'teacher': [],
                'updated_at': '1987-06-07T00:00:00',
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
            'created_at': '1987-06-07T00:00:00',
            'email': None,
            'is_active': False,
            'name': 'Two',
            'surname': 'student',
            'teacher': [1],
            'updated_at': '1987-06-07T00:00:00',
        }

        self.assertEqual(response.json(), base_response)

    def test_student_update(self):
        students = Student.objects.all()
        response = self.client.put(reverse('students_api-detail',
                                           kwargs={'pk': students[0].id}),
                                   {
                                        'name': 'Two',
                                        'surname': 'student',
                                        'teacher': [1],
                                   })
        base_response = {
            'created_at': '1987-06-07T00:00:00',
            'email': None,
            'is_active': False,
            'name': 'Two',
            'surname': 'student',
            'teacher': [1],
            'updated_at': '1987-06-07T00:00:00',
        }

        self.assertEqual(response.json(), base_response)

    def test_student_delete(self):
        students = Student.objects.all()
        self.assertEqual(students.count(), 1)

        self.client.delete(reverse('students_api-detail',
                                   kwargs={'pk': students[0].id}))

        self.assertEqual(students.count(), 0)


@freezegun.freeze_time('1987-06-07 00:00:00')
class SubjectApiTest(APITestCase):

    def setUp(self) -> None:
        Subject.objects.create(title='Python')

    def test_subject_view(self):
        self.client.get(reverse('subject_api-list'))
        subjects = Subject.objects.all()
        self.assertEqual(subjects.count(), 1)

    def test_subject_create(self):
        response = self.client.post(reverse('subject_api-list'),
                                    {
            'title': 'Java',
        })

        base_response = {
            'created_at': '1987-06-07T00:00:00',
            'id': 2,
            'title': 'Java',
            'updated_at': '1987-06-07T00:00:00',
        }
        self.assertEqual(response.json(), base_response)

    def test_subject_update(self):
        subjects = Subject.objects.all()
        response = self.client.put(reverse('subject_api-detail',
                                           kwargs={'pk': subjects[0].id}),
                                   {
            'title': 'JavaScript'
        })

        base_response = {
            'created_at': '1987-06-07T00:00:00',
            'id': 1,
            'title': 'JavaScript',
            'updated_at': '1987-06-07T00:00:00',
        }
        self.assertEqual(response.json(), base_response)

    def test_subject_delete(self):
        subjects = Subject.objects.all()
        self.assertEqual(subjects.count(), 1)

        self.client.delete(reverse('subject_api-detail',
                                   kwargs={'pk': subjects[0].id}))

        self.assertEqual(subjects.count(), 0)


@freezegun.freeze_time('1987-06-07 00:00:00')
class ReportCardApiTest(APITestCase):

    def setUp(self) -> None:
        ReportCard.objects.create(report_card='zachetka')

    def test_report_card_view(self):
        self.client.get(reverse('report_card_api-list'))
        report_cards = ReportCard.objects.all()
        self.assertEqual(report_cards.count(), 1)

    def test_report_card_create(self):
        response = self.client.post(reverse('report_card_api-list'),
                                    {
            'report_card': 'zachetka_v_2_0',
        })

        base_response = {
            'created_at': '1987-06-07T00:00:00',
            'id': 2,
            'report_card': 'zachetka_v_2_0',
            'updated_at': '1987-06-07T00:00:00',
        }
        self.assertEqual(response.json(), base_response)

    def test_report_cart_update(self):
        report_cards = ReportCard.objects.all()
        response = self.client.put(reverse('report_card_api-detail',
                                           kwargs={'pk': report_cards[0].id}),
                                   {
            'report_card': 'zachetka_v_2_0'
        })

        base_response = {
            'created_at': '1987-06-07T00:00:00',
            'id': 1,
            'report_card': 'zachetka_v_2_0',
            'updated_at': '1987-06-07T00:00:00',
        }
        self.assertEqual(response.json(), base_response)

    def test_report_card_delete(self):
        report_cards = ReportCard.objects.all()
        self.assertEqual(report_cards.count(), 1)

        self.client.delete(reverse('report_card_api-detail',
                                   kwargs={'pk': report_cards[0].id}))
        self.assertEqual(report_cards.count(), 0)


@freezegun.freeze_time('1987-06-07 00:00:00')
class TeacherApiTest(APITestCase):

    def setUp(self) -> None:
        Teacher.objects.create(name_surname='Rick Sanchez')

    def test_teacher_view(self):
        self.client.get(reverse('teacher_api-list'))
        teachers = Teacher.objects.all()
        self.assertEqual(teachers.count(), 1)

    def test_teacher_create(self):
        response = self.client.post(reverse('teacher_api-list'), {
            'name_surname': 'Morty Smith'
        })

        base_response = {
            'created_at': '1987-06-07T00:00:00',
            'id': 2,
            'name_surname': 'Morty Smith',
            'updated_at': '1987-06-07T00:00:00',
        }

        self.assertEqual(response.json(), base_response)

    def test_teacher_update(self):
        teachers = Teacher.objects.all()
        response = self.client.put(reverse('teacher_api-detail',
                                           kwargs={'pk': teachers[0].id}),
                                   {
            'name_surname': 'Morty Smith'
        })

        base_response = {
            'created_at': '1987-06-07T00:00:00',
            'id': 1,
            'name_surname': 'Morty Smith',
            'updated_at': '1987-06-07T00:00:00',
        }

        self.assertEqual(response.json(), base_response)

    def test_teacher_delete(self):
        teachers = Teacher.objects.all()
        self.assertEqual(teachers.count(), 1)

        self.client.delete(reverse('teacher_api-detail',
                                   kwargs={'pk': teachers[0].id}))
        self.assertEqual(teachers.count(), 0)
