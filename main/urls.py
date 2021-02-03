"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from .api.student import views as student_view
from .api.teacher import views as teacher_view
from .api.section import views as section_view
from .views import api_get_stat
from django.contrib import admin
from django.urls import path

app_name = 'main'

urlpatterns = [
    path('api/get_stat', api_get_stat, name='get_stat'),

    #Student URL
    path('api/all_student', student_view.api_get_all_student, name='get_all_student'),
    path('api/get_student', student_view.api_get_student, name='get_student'),
    path('api/add_student', student_view.api_add_student, name='add_student'),
    path('api/update_student', student_view.api_update_student, name='update_student'),
    path('api/delete_student', student_view.api_delete_student, name='delete_student'),


    #Teacher URL
    path('api/all_teacher', teacher_view.api_get_all_teacher, name='get_all_teacher'),
    path('api/get_teacher', teacher_view.api_get_teacher, name='get_teacher'),
    path('api/add_teacher', teacher_view.api_add_teacher, name='add_teacher'),
    path('api/update_teacher', teacher_view.api_update_teacher, name='update_teacher'),
    path('api/delete_teacher', teacher_view.api_delete_teacher, name='delete_teacher'),
    
    
    #Section URL
    path('api/all_section', section_view.api_get_all_section, name='get_all_section'),
    path('api/assign_section', section_view.api_set_section, name='set_section'),
    path('api/add_section', section_view.api_add_section, name='add_section'),
    path('api/get_section_student', section_view.api_get_section_student, name='section_student'),
]
