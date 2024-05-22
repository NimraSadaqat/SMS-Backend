from rest_framework import serializers
from .models import Fees, StudentFee, FeeReceipt

class FeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fees
        fields = '__all__'

class StudentFeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentFee
        fields = '__all__'

class FeeReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeeReceipt
        fields = '__all__'
