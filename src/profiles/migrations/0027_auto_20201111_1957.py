# Generated by Django 3.1.2 on 2020-11-11 19:57

import datetime
from django.db import migrations, models
import profiles.models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0026_auto_20201111_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='date',
            field=models.DateTimeField(choices=[(datetime.datetime(2020, 11, 18, 19, 57, 22, 666593), '1 week'), (datetime.datetime(2020, 11, 12, 19, 57, 22, 666574), 'tomorrow'), (datetime.datetime(2020, 12, 11, 19, 57, 22, 666596), '1 month'), (datetime.datetime(2020, 11, 25, 19, 57, 22, 666595), '2 weeks')], default=profiles.models.tomorrow),
        ),
        migrations.AlterField(
            model_name='goal',
            name='goal_type',
            field=models.IntegerField(choices=[(0, 'Exercise'), (1, 'Nutrition'), (3, 'Appointment'), (2, 'Sleep')], default=0),
        ),
    ]
