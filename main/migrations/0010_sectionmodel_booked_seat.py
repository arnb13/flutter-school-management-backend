# Generated by Django 3.1.3 on 2020-11-21 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20201121_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='sectionmodel',
            name='booked_seat',
            field=models.IntegerField(default=0),
        ),
    ]
