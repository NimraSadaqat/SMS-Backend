from rest_framework.response import Response
from django.utils.translation import gettext as _
from django.shortcuts import get_object_or_404
from rest_framework.status import (
    HTTP_200_OK, HTTP_201_CREATED, HTTP_406_NOT_ACCEPTABLE,
    HTTP_405_METHOD_NOT_ALLOWED
)
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from .models import Fees, StudentFee, FeeReceipt
from .serializers import FeesSerializer, StudentFeeSerializer, FeeReceiptSerializer

class FeesAPI(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        queryset = Fees.objects.all()
        serializer = FeesSerializer(queryset, many=True)
        return Response({
            "success": True, "data": serializer.data, "message": ""
        }, status=HTTP_200_OK
        )

    def post(self, request, format=None):
        data = request.data

        serializer = FeesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True, "data": data, 'message': _('Saved')
            }, status=HTTP_201_CREATED
            )
        else:
            return Response({
                'success': False, "data": serializer.errors, 'message': _('Could not save')
            }, status=HTTP_406_NOT_ACCEPTABLE
            )

class FeesDetailAPI(APIView):
    """
    Retrieve, update or delete a Fees instance.
    """
    permission_classes = (AllowAny,)

    def get(self, request, pk, format=None):
        fees = get_object_or_404(Fees, pk=pk)
        serializer = FeesSerializer(fees)
        return Response({
            'success': True,
            'data': serializer.data,
            'message': ""
        }, status=HTTP_200_OK)

    def put(self, request, pk, format=None):
        fees = get_object_or_404(Fees, pk=pk)
        serializer = FeesSerializer(fees, data=request.data)

        if serializer.is_valid():
            # print(serializer.validated_data)
            serializer.save()
            return Response({
                'success': True, 'data': serializer.data, 'message': _('Updated')
            }, status=HTTP_200_OK)
        else:
            return Response({
                'success': False, "data": serializer.errors, 'message': _('Could not update')
            }, status=HTTP_406_NOT_ACCEPTABLE
            )

    def delete(self, request, pk, format=None):
        return Response({
            'success': False, "data": None, 'message': _("Method 'DELETE' not allowed")
        }, status=HTTP_405_METHOD_NOT_ALLOWED
        )
    
class StudentFeeAPI(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        queryset = StudentFee.objects.all()
        serializer = StudentFeeSerializer(queryset, many=True)
        return Response({
            "success": True, "data": serializer.data, "message": ""
        }, status=HTTP_200_OK
        )

    def post(self, request, format=None):
        data = request.data

        serializer = StudentFeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True, "data": data, 'message': _('Saved')
            }, status=HTTP_201_CREATED
            )
        else:
            return Response({
                'success': False, "data": serializer.errors, 'message': _('Could not save')
            }, status=HTTP_406_NOT_ACCEPTABLE
            )

class StudentFeeDetailAPI(APIView):
    """
    Retrieve, update or delete a StudentFee instance.
    """
    permission_classes = (AllowAny,)

    def get(self, request, pk, format=None):
        studentFee = get_object_or_404(StudentFee, pk=pk)
        serializer = StudentFeeSerializer(studentFee)
        return Response({
            'success': True,
            'data': serializer.data,
            'message': ""
        }, status=HTTP_200_OK)

    def put(self, request, pk, format=None):
        studentFee = get_object_or_404(StudentFee, pk=pk)
        serializer = StudentFeeSerializer(studentFee, data=request.data)

        if serializer.is_valid():
            # print(serializer.validated_data)
            serializer.save()
            return Response({
                'success': True, 'data': serializer.data, 'message': _('Updated')
            }, status=HTTP_200_OK)
        else:
            return Response({
                'success': False, "data": serializer.errors, 'message': _('Could not update')
            }, status=HTTP_406_NOT_ACCEPTABLE
            )

    def delete(self, request, pk, format=None):
        return Response({
            'success': False, "data": None, 'message': _("Method 'DELETE' not allowed")
        }, status=HTTP_405_METHOD_NOT_ALLOWED
        )
    
class FeeReceiptAPI(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        queryset = FeeReceipt.objects.all()
        serializer = FeeReceiptSerializer(queryset, many=True)
        return Response({
            "success": True, "data": serializer.data, "message": ""
        }, status=HTTP_200_OK
        )

    def post(self, request, format=None):
        data = request.data

        serializer = FeeReceiptSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True, "data": data, 'message': _('Saved')
            }, status=HTTP_201_CREATED
            )
        else:
            return Response({
                'success': False, "data": serializer.errors, 'message': _('Could not save')
            }, status=HTTP_406_NOT_ACCEPTABLE
            )

class FeeReceiptDetailAPI(APIView):
    """
    Retrieve, update or delete a FeeReceipt instance.
    """
    permission_classes = (AllowAny,)

    def get(self, request, pk, format=None):
        feeReceipt = get_object_or_404(FeeReceipt, pk=pk)
        serializer = FeeReceiptSerializer(feeReceipt)
        return Response({
            'success': True,
            'data': serializer.data,
            'message': ""
        }, status=HTTP_200_OK)

    def put(self, request, pk, format=None):
        feeReceipt = get_object_or_404(FeeReceipt, pk=pk)
        serializer = FeeReceiptSerializer(feeReceipt, data=request.data)

        if serializer.is_valid():
            # print(serializer.validated_data)
            serializer.save()
            return Response({
                'success': True, 'data': serializer.data, 'message': _('Updated')
            }, status=HTTP_200_OK)
        else:
            return Response({
                'success': False, "data": serializer.errors, 'message': _('Could not update')
            }, status=HTTP_406_NOT_ACCEPTABLE
            )

    def delete(self, request, pk, format=None):
        return Response({
            'success': False, "data": None, 'message': _("Method 'DELETE' not allowed")
        }, status=HTTP_405_METHOD_NOT_ALLOWED
        )