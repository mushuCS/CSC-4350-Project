# Generated by Django 3.1.2 on 2020-11-09 19:42

import datetime
from django.db import migrations, models
import goals.models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0008_auto_20201109_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='date',
            field=models.DateTimeField(choices=[(datetime.datetime(2020, 11, 23, 19, 42, 38, 178392), '2 weeks'), (datetime.datetime(2020, 12, 9, 19, 42, 38, 178393), '1 month'), (datetime.datetime(2020, 11, 10, 19, 42, 38, 178377), 'tomorrow'), (datetime.datetime(2020, 11, 16, 19, 42, 38, 178390), '1 week')], default=goals.models.tomorrow),
        ),
        migrations.AlterField(
            model_name='goal',
            name='goal_type',
            field=models.IntegerField(choices=[(3, 'Appointment'), (1, 'Nutrition'), (2, 'Sleep'), (0, 'Exercise')], default=0),
        ),
    ]
