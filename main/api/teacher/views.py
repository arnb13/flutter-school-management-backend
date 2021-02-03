from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.serializers import Serializer


from ...models import StudentModel, TeacherModel, SectionModel, AssignedSectionModel
from ...serializers import StudentSerializer, TeacherSerializer, SectionSerializer, AssignedSerializer
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def api_get_all_teacher(request):
    content = {}
    try:
        teacher = TeacherModel.objects.all()
        serizlizer = TeacherSerializer(teacher, many = True)
        return Response(serizlizer.data, status= status.HTTP_200_OK)
    except:
        content = {'status': 'teacher not found'}
        return Response(content, status= status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def api_add_teacher(request):
    content = {}
    teacher = TeacherModel()
    serializer = TeacherSerializer(teacher, request.data)

    if serializer.is_valid():
        success = serializer.save()

        if success:
            content = {'status': 'teacher created'}
            return Response(content, status= status.HTTP_200_OK)
        else:
            content = {'status': 'teacher not created'}
            return Response(content, status= status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def api_get_teacher(request):
    sections = []
    content = {}
    try:
        teacher = TeacherModel.objects.get(email = request.data['email'])
        try:
            sectionsModel = SectionModel.objects.filter(fk_teacher = teacher.id)
            serializer2 = SectionSerializer(sectionsModel, many = True)

            for i in serializer2.data:
                sections.append(i['section_number'])
        except:
            pass

        serializer1 = TeacherSerializer(teacher)
        
    except:
        content = {'status': 'student info not found'}
        return Response(content, status= status.HTTP_404_NOT_FOUND)

    content = {
        'teacher': serializer1.data,
        'section': sections
        }


    return Response(content, status= status.HTTP_200_OK)


@api_view(['POST'])
def api_update_teacher(request):
    content = {}
    try:
        teacher = TeacherModel.objects.get(email = request.data['email'])
        serializer = TeacherSerializer(teacher, request.data, partial = True)
        

        if serializer.is_valid():
            success = serializer.save()
            

            if success:
                content = {'status': 'teacher info updated'}
                return Response(content, status= status.HTTP_200_OK)
            else:
                content = {'status': 'teacher info update error'}
                return Response(content, status= status.HTTP_400_BAD_REQUEST)

    except:
        content = {'status': 'email not found'}
        return Response(content, status= status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def api_delete_teacher(request):
    content = {}
    try:
        teacher = TeacherModel.objects.get(email = request.data['email'])
        
        try:
            sections = SectionModel.objects.filter(fk_teacher = teacher.id)
            for section in sections:

                section.fk_teacher = None
                section.save()

        except:
            content = {'section': 'no section found'}
        
        teacher.delete()
        content = {'status': 'teacher deleted successfully'}
        return Response(content, status= status.HTTP_200_OK)


    except:
        content = {'status': 'teacher not found'}
        return Response(content, status= status.HTTP_400_BAD_REQUEST)
    
