# Generated by Django 3.1.2 on 2020-11-11 19:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import goals.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('goals', '0021_auto_20201110_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='goal_type',
            field=models.IntegerField(choices=[(2, 'Sleep'), (0, 'Exercise'), (1, 'Nutrition'), (3, 'Appointment')], default=0),
        ),
        migrations.AlterField(
            model_name='goal',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]