from django.urls import path
from .api import (StudentAPI, StudentDetailAPI, 
                  FamilyInformationAPI, FamilyInformationDetailAPI)

urlpatterns = [
    path('', StudentAPI.as_view(), name='student-list'),
    path('<int:pk>/', StudentDetailAPI.as_view(), name='student-detail'),
    path('family/', FamilyInformationAPI.as_view(), name='family-list'),
    path('family/<int:pk>/', FamilyInformationDetailAPI.as_view(), name='family-detail'),
]