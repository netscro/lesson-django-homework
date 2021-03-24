from rest_framework import serializers

from home.models import ReportCard, Student, Subject, Teacher


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'surname', 'email', 'is_active', 'teacher', 'created_at', 'updated_at']


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'title', 'created_at', 'updated_at']


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'name_surname', 'created_at', 'updated_at']


class ReportCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportCard
        fields = ['id', 'report_card', 'created_at', 'updated_at']
