from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.serializers import Serializer


from ...models import StudentModel, TeacherModel, SectionModel, AssignedSectionModel
from ...serializers import StudentSerializer, TeacherSerializer, SectionSerializer, AssignedSerializer
from rest_framework.response import Response

# Create your views here.

@api_view(['POST'])
def api_get_student(request):
    sections = []
    content = {}
    try:
        student = StudentModel.objects.get(roll = request.data['roll'])
        serializer1 = StudentSerializer(student)
        try:
            assigned_sections = AssignedSectionModel.objects.filter(fk_student = student.id)
            serializer2 = AssignedSerializer(assigned_sections, many = True)
            for i in serializer2.data:
                sections.append(i['fk_section']['section_number'])
        except:
            pass
    except:
        content = {'status': 'student info not found'}
        return Response(content, status= status.HTTP_404_NOT_FOUND)

    content = {
        'student': serializer1.data,
        'section': sections
        }

    return Response(content, status= status.HTTP_200_OK)



@api_view(['GET'])
def api_get_all_student(request):
    content = {}
    try:
        student = StudentModel.objects.all()
        serizlizer = StudentSerializer(student, many = True)
        return Response(serizlizer.data, status= status.HTTP_200_OK)
    except:
        content = {'status': 'student info not found'}
        return Response(content, status= status.HTTP_404_NOT_FOUND)



@api_view(['POST'])
def api_add_student(request):
    content = {}
    try:
        student = StudentModel.objects.get(roll = request.data['roll'])
        content = {'status': 'Roll not unique'}
        return Response(content, status= status.HTTP_400_BAD_REQUEST)
    except:
        student = StudentModel()
        serializer = StudentSerializer(student, request.data)

        if serializer.is_valid():
            success = serializer.save()

            if success:
                content = {'status': 'student created'}
                return Response(content, status= status.HTTP_200_OK)
            else:
                content = {'status': 'student not created'}
                return Response(content, status= status.HTTP_400_BAD_REQUEST)
    


@api_view(['POST'])
def api_update_student(request):
    content = {}
    try:
        student = StudentModel.objects.get(roll = request.data['roll'])
        serializer = StudentSerializer(student, request.data, partial = True)
        

        if serializer.is_valid():
            success = serializer.save()
            

            if success:
                content = {'status': 'student info updated'}
                return Response(content, status= status.HTTP_200_OK)
            else:
                content = {'status': 'student info update error'}
                return Response(content, status= status.HTTP_400_BAD_REQUEST)

    except:
        content = {'status': 'Roll not found'}
        return Response(content, status= status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def api_delete_student(request):
    content = {}
    try:
        student = StudentModel.objects.get(roll = request.data['roll'])
        
        try:
            assigned_sections = AssignedSectionModel.objects.filter(fk_student = student.id)
            assigned_sections.delete()
        except:
            content = {'section': 'no section assigned'}
        
        student.delete()
        content = {'status': 'student deleted successfully'}
        return Response(content, status= status.HTTP_200_OK)
    
    except:
        content = {'status': 'student not found'}
        return Response(content, status= status.HTTP_400_BAD_REQUEST)



