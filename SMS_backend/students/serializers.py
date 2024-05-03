from rest_framework import serializers, fields
from students.models import (Student, FamilyInformation)

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class FamilyInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyInformation
        fields = '__all__'