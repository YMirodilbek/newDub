# Generated by Django 5.1.2 on 2024-11-11 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0147_person_room_luxury_rooms_service_department'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room_luxury',
            name='kv1',
        ),
        migrations.RemoveField(
            model_name='room_luxury',
            name='price1',
        ),
        migrations.RemoveField(
            model_name='rooms',
            name='kv1',
        ),
        migrations.RemoveField(
            model_name='rooms',
            name='price1',
        ),
    ]
