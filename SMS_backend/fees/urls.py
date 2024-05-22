from django.urls import path
from .api import (FeesAPI, FeesDetailAPI,
                  StudentFeeAPI, StudentFeeDetailAPI,
                  FeeReceiptAPI, FeeReceiptDetailAPI)

urlpatterns = [
    path('', FeesAPI.as_view(), name='fees-list'),
    path('<int:pk>/', FeesDetailAPI.as_view(), name='fees-detail'),
    path('student/', StudentFeeAPI.as_view(), name='student_fee-list'),
    path('student/<int:pk>/', StudentFeeDetailAPI.as_view(), name='student_fee-detail'),
    path('receipt/', FeeReceiptAPI.as_view(), name='fee_receipt-list'),
    path('receipt/<int:pk>/', FeeReceiptDetailAPI.as_view(), name='fee_receipt-detail'),
]
