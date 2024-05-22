from django.urls import path
from .api import AcademicYearAPI, AcademicYearDetailAPI

urlpatterns = [
    path('', AcademicYearAPI.as_view(), name='academic_year-list'),
    path('<int:pk>/', AcademicYearDetailAPI.as_view(), name='academic_year-detail'),
]
