# Generated by Django 5.1.2 on 2024-11-01 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0087_project_kard_href'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project_kard',
            name='href',
        ),
    ]
