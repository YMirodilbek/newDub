# Generated by Django 5.1.2 on 2024-10-13 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0050_rename_kard_project_kard'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rasm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rasm', models.ImageField(upload_to='media/')),
            ],
        ),
    ]
