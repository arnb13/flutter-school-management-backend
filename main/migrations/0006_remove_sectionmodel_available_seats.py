# Generated by Django 3.1.3 on 2020-11-21 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20201121_2224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sectionmodel',
            name='available_seats',
        ),
    ]
