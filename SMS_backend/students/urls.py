from django.urls import path
from . import api

urlpatterns = [
    path('', api.StudentListView.as_view(), name='student-list'),
    path('create/', api.StudentCreateView.as_view(), name='student-create'),
]