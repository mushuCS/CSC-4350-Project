# Generated by Django 3.1.2 on 2020-11-09 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0006_auto_20201109_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='goal_type',
            field=models.IntegerField(choices=[(2, 'Sleep'), (1, 'Nutrition'), (3, 'Appointment'), (0, 'Exercise')], default=0),
        ),
    ]
