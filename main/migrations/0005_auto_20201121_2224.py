# Generated by Django 3.1.3 on 2020-11-21 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_sectionmodel_available_seats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sectionmodel',
            name='available_seats',
            field=models.IntegerField(default=0),
        ),
    ]
