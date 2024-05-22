from rest_framework import serializers
from .models import Academic_Year

class AcademicYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Academic_Year
        fields = '__all__'
