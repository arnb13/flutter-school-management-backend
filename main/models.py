from django.db import models

# Create your models here.

class StudentModel(models.Model):
    id = models.AutoField(auto_created= True, primary_key= True, unique= True, editable= False)
    first_name = models.CharField(max_length=200, default = '-1')
    last_name = models.CharField(max_length=200, default = '-1')
    roll = models.CharField(max_length=200, unique= True, default = '-1')
    email = models.CharField(max_length= 250, unique= True, default= '-1')
    phone = models.CharField (max_length= 15, unique= True, default= '-1')
    is_active = models.BooleanField(default= True)

    def __str__ (self) :
        return self.first_name

class TeacherModel(models.Model):
    id = models.AutoField(auto_created= True, primary_key= True, unique= True, editable= False)
    first_name = models.CharField(max_length=200, default = '-1')
    last_name = models.CharField(max_length=200, default = '-1')
    email = models.CharField(max_length= 250, unique= True, default= '-1')
    phone = models.CharField (max_length= 15, unique= True, default= '-1')
    is_active = models.BooleanField(default= True)

    def __str__ (self) :
        return self.first_name


class SectionModel (models.Model):
    id = models.AutoField(auto_created= True, primary_key= True, unique= True, editable= False)
    section_number = models.CharField(max_length=200, unique= True, default = '-1')
    total_seat = models.IntegerField(default= 0)
    booked_seat = models.IntegerField(default= 0)
    available_seat = models.IntegerField(default= 0)
    is_active = models.BooleanField(default= True)

    fk_teacher = models.ForeignKey (TeacherModel, default = -1, on_delete = models.SET_DEFAULT, null= True, blank= True)

    def __str__ (self) :
        return self.section_number

class AssignedSectionModel(models.Model):
    id = models.AutoField(auto_created= True, primary_key= True, unique= True, editable= False)
    is_active = models.BooleanField(default= True)

    fk_student = models.ForeignKey (StudentModel, default = -1, on_delete = models.SET_DEFAULT)
    fk_section = models.ForeignKey (SectionModel, default = -1, on_delete = models.SET_DEFAULT)

    def __str__ (self) :
        return self.fk_student.first_name


