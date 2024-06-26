from rest_framework.response import Response
from django.utils.translation import gettext as _
from django.shortcuts import get_object_or_404
from rest_framework.status import (
    HTTP_200_OK, HTTP_201_CREATED, HTTP_406_NOT_ACCEPTABLE,
    HTTP_405_METHOD_NOT_ALLOWED
)
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from .models import Student, FamilyInformation
from .serializers import StudentSerializer, FamilyInformationSerializer

class FamilyInformationAPI(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        queryset = FamilyInformation.objects.all()
        serializer = FamilyInformationSerializer(queryset, many=True)
        return Response({
            "success": True, "data": serializer.data, "message": ""
        }, status=HTTP_200_OK
        )

    def post(self, request, format=None):
        data = request.data

        serializer = FamilyInformationSerializer(data=request.data)
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

class FamilyInformationDetailAPI(APIView):
    """
    Retrieve, update or delete a FamilyInformation instance.
    """
    permission_classes = (AllowAny,)

    def get(self, request, pk, format=None):
        familyInformation = get_object_or_404(FamilyInformation, pk=pk)
        serializer = FamilyInformationSerializer(familyInformation)
        return Response({
            'success': True,
            'data': serializer.data,
            'message': ""
        }, status=HTTP_200_OK)

    def put(self, request, pk, format=None):
        familyInformation = get_object_or_404(FamilyInformation, pk=pk)
        serializer = FamilyInformationSerializer(familyInformation, data=request.data)

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


class StudentAPI(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        return Response({
            "success": True, "data": serializer.data, "message": ""
        }, status=HTTP_200_OK
        )

    def post(self, request, format=None):
        data = request.data

        serializer = StudentSerializer(data=request.data)
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

class StudentDetailAPI(APIView):
    """
    Retrieve, update or delete a Student instance.
    """
    permission_classes = (AllowAny,)

    def get(self, request, pk, format=None):
        student = get_object_or_404(Student, pk=pk)
        serializer = StudentSerializer(student)
        return Response({
            'success': True,
            'data': serializer.data,
            'message': ""
        }, status=HTTP_200_OK)

    def put(self, request, pk, format=None):
        student = get_object_or_404(Student, pk=pk)
        serializer = StudentSerializer(student, data=request.data)

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
