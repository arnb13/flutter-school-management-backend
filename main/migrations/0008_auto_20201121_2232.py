# Generated by Django 3.1.3 on 2020-11-21 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_sectionmodel_available_seats'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sectionmodel',
            name='available_seats',
        ),
        migrations.AddField(
            model_name='sectionmodel',
            name='available_seat',
            field=models.CharField(default='0', max_length=250),
        ),
    ]
