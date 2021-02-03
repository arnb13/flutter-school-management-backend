from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.serializers import Serializer


from .models import StudentModel, TeacherModel, SectionModel, AssignedSectionModel
from .serializers import StudentSerializer, TeacherSerializer, SectionSerializer, AssignedSerializer
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def api_get_stat(request):
    content = {}
    try:
        total_student = StudentModel.objects.all().count()
        total_teacher = TeacherModel.objects.all().count()
        total_section = SectionModel.objects.all()
        available = 0
        total_seats = 0
        total_booked = 0
        for i in total_section:
            total_seats = total_seats + i.total_seat
            total_booked = total_booked + i.booked_seat
            available = available + i.available_seat

    except:
        content = {'status': 'error retrieving stats'}
        return Response(content, status= status.HTTP_400_BAD_REQUEST)
    
    content = {
        'total_student': total_student,
        'total_teacher': total_teacher,
        'total_section': total_section.count(),
        'total_seat': total_seats,
        'booked_seat': total_booked, 
        'available_seat': available
    }

    return Response(content, status= status.HTTP_200_OK)
    
