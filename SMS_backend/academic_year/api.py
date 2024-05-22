from rest_framework.response import Response
from django.utils.translation import gettext as _
from django.shortcuts import get_object_or_404
from rest_framework.status import (
    HTTP_200_OK, HTTP_201_CREATED, HTTP_406_NOT_ACCEPTABLE,
    HTTP_405_METHOD_NOT_ALLOWED
)
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from .models import Academic_Year
from .serializers import AcademicYearSerializer

class AcademicYearAPI(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        queryset = Academic_Year.objects.all()
        serializer = AcademicYearSerializer(queryset, many=True)
        return Response({
            "success": True, "data": serializer.data, "message": ""
        }, status=HTTP_200_OK
        )

    def post(self, request, format=None):
        data = request.data

        serializer = AcademicYearSerializer(data=request.data)
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

class AcademicYearDetailAPI(APIView):
    """
    Retrieve, update or delete a Academic_Year instance.
    """
    permission_classes = (AllowAny,)

    def get(self, request, pk, format=None):
        academicYear = get_object_or_404(Academic_Year, pk=pk)
        serializer = AcademicYearSerializer(academicYear)
        return Response({
            'success': True,
            'data': serializer.data,
            'message': ""
        }, status=HTTP_200_OK)

    def put(self, request, pk, format=None):
        academicYear = get_object_or_404(Academic_Year, pk=pk)
        serializer = AcademicYearSerializer(academicYear, data=request.data)

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