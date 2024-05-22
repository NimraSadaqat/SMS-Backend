from rest_framework.response import Response
from django.utils.translation import gettext as _
from django.shortcuts import get_object_or_404
from rest_framework.status import (
    HTTP_200_OK, HTTP_201_CREATED, HTTP_406_NOT_ACCEPTABLE,
    HTTP_405_METHOD_NOT_ALLOWED
)
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from .models import EmployeeInformation, Salary
from .serializers import EmployeeInformationSerializer, SalarySerializer

class EmployeeInformationAPI(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        queryset = EmployeeInformation.objects.all()
        serializer = EmployeeInformationSerializer(queryset, many=True)
        return Response({
            "success": True, "data": serializer.data, "message": ""
        }, status=HTTP_200_OK
        )

    def post(self, request, format=None):
        data = request.data

        serializer = EmployeeInformationSerializer(data=request.data)
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

class EmployeeInformationDetailAPI(APIView):
    """
    Retrieve, update or delete a EmployeeInformation instance.
    """
    permission_classes = (AllowAny,)

    def get(self, request, pk, format=None):
        employeeInformation = get_object_or_404(EmployeeInformation, pk=pk)
        serializer = EmployeeInformationSerializer(employeeInformation)
        return Response({
            'success': True,
            'data': serializer.data,
            'message': ""
        }, status=HTTP_200_OK)

    def put(self, request, pk, format=None):
        employeeInformation = get_object_or_404(EmployeeInformation, pk=pk)
        serializer = EmployeeInformationSerializer(employeeInformation, data=request.data)

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
    
class SalaryAPI(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        queryset = Salary.objects.all()
        serializer = SalarySerializer(queryset, many=True)
        return Response({
            "success": True, "data": serializer.data, "message": ""
        }, status=HTTP_200_OK
        )

    def post(self, request, format=None):
        data = request.data

        serializer = SalarySerializer(data=request.data)
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

class SalaryDetailAPI(APIView):
    """
    Retrieve, update or delete a Salary instance.
    """
    permission_classes = (AllowAny,)

    def get(self, request, pk, format=None):
        salary = get_object_or_404(Salary, pk=pk)
        serializer = SalarySerializer(salary)
        return Response({
            'success': True,
            'data': serializer.data,
            'message': ""
        }, status=HTTP_200_OK)

    def put(self, request, pk, format=None):
        salary = get_object_or_404(Salary, pk=pk)
        serializer = SalarySerializer(salary, data=request.data)

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