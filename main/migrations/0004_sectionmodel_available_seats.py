# Generated by Django 3.1.3 on 2020-11-21 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20201121_0418'),
    ]

    operations = [
        migrations.AddField(
            model_name='sectionmodel',
            name='available_seats',
            field=models.IntegerField(default=0),
        ),
    ]
