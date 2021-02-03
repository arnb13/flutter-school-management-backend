from django.contrib import admin
from .models import StudentModel, TeacherModel, SectionModel, AssignedSectionModel

# Register your models here.

admin.site.register(StudentModel)
admin.site.register(TeacherModel)
admin.site.register(SectionModel)
admin.site.register(AssignedSectionModel)

