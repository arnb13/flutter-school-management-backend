# Generated by Django 3.1.3 on 2020-11-19 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(default='-1', max_length=200)),
                ('last_name', models.CharField(default='-1', max_length=200)),
                ('roll', models.CharField(default='-1', max_length=200)),
                ('email', models.CharField(default='-1', max_length=250, unique=True)),
                ('phone', models.CharField(default='-1', max_length=15, unique=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='TeacherModel',
            fields=[
                ('id', models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(default='-1', max_length=200)),
                ('last_name', models.CharField(default='-1', max_length=200)),
                ('email', models.CharField(default='-1', max_length=250, unique=True)),
                ('phone', models.CharField(default='-1', max_length=15, unique=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='SectionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False, unique=True)),
                ('section_number', models.CharField(default='-1', max_length=200)),
                ('total_seat', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('fk_teacher', models.ForeignKey(default=-1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.teachermodel')),
            ],
        ),
        migrations.CreateModel(
            name='AssignedSectionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('fk_section', models.ForeignKey(default=-1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.sectionmodel')),
                ('fk_student', models.ForeignKey(default=-1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.studentmodel')),
            ],
        ),
    ]
