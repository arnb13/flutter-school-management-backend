from rest_framework import serializers
from .models import StudentModel, TeacherModel, SectionModel, AssignedSectionModel

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = ['id', 'first_name', 'last_name', 'roll', 'email', 'phone']

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherModel
        fields = ['id', 'first_name', 'last_name', 'email', 'phone']

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionModel
        fields = ['id', 'section_number', 'total_seat', 'available_seat', 'fk_teacher']

class AssignedSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignedSectionModel
        fields = ['id', 'fk_section']
        depth = 1