from rest_framework import generics, permissions
from .models import Student, FamilyInformation
from .serializers import StudentSerializer, FamilyInformationSerializer

class StudentCreateView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['post']

class StudentListView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    http_method_names = ['get']