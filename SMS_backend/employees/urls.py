from django.urls import path
from .api import (EmployeeInformationAPI, EmployeeInformationDetailAPI,
                  SalaryAPI, SalaryDetailAPI)
                

urlpatterns = [
    path('', EmployeeInformationAPI.as_view(), name='employee_information-list'),
    path('<int:pk>/', EmployeeInformationDetailAPI.as_view(), name='academic_year-detail'),
    path('salary/', SalaryAPI.as_view(), name='employee_salary-list'),
    path('salary/<int:pk>/', SalaryDetailAPI.as_view(), name='employee_salary-detail'),
]
