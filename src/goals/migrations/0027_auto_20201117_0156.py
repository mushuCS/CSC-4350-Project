# Generated by Django 3.1.2 on 2020-11-17 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0026_auto_20201111_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='goal_type',
            field=models.IntegerField(choices=[(3, 'Appointment'), (0, 'Exercise'), (1, 'Nutrition'), (2, 'Sleep')], default=0),
        ),
    ]