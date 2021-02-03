from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.serializers import Serializer


from ...models import StudentModel, TeacherModel, SectionModel, AssignedSectionModel
from ...serializers import StudentSerializer, TeacherSerializer, SectionSerializer, AssignedSerializer
from rest_framework.response import Response

# Create your views here

@api_view(['GET'])
def api_get_all_section(request):
    content = {}
    try:
        section = SectionModel.objects.all().order_by('section_number')
        serizlizer = SectionSerializer(section, many = True)
        return Response(serizlizer.data, status= status.HTTP_200_OK)
    except:
        content = {'status': 'teacher not found'}
        return Response(content, status= status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def api_set_section(request):
    content = {}
    student = StudentModel.objects.get(roll = request.data['roll'])
    section = SectionModel.objects.get(section_number = request.data['section'])
    assign = AssignedSectionModel()
    assign.fk_student = student
    assign.fk_section = section

    serializer = AssignedSerializer(assign, request.data)

    if serializer.is_valid():
        success = serializer.save()

        if success:
            section.available_seat = section.available_seat - 1
            section.save()
            content = {'status': 'section assigned'}
            return Response(content, status= status.HTTP_200_OK)


@api_view(['GET'])
def api_get_section_student(request):
    content = {}
    try:
        sectionId = SectionModel.objects.get(section_number = request.data['section_number'])
        section = AssignedSectionModel.objects.filter(fk_section = sectionId.id)
        serializer = AssignedSerializer(section, many = True)
    except:
        content = {'status': 'section not found'}
        return Response(content, status= status.HTTP_404_NOT_FOUND)

    return Response(serializer.data, status= status.HTTP_200_OK)


@api_view(['GET'])
def api_add_section(request):
    content = {}
    try:
        section = SectionModel()
        teacher = TeacherModel.objects.get(email = request.data['email'])
        section.fk_teacher = teacher
        serializer = SectionSerializer(section, request.data)

        if serializer.is_valid():
            success = serializer.save()
            if success:
                content = {'status': 'section added'}
                return Response(content, status= status.HTTP_200_OK)

        
    except:
        content = {'status': 'section not added'}
        return Response(content, status= status.HTTP_404_NOT_FOUND)

    
    
    



