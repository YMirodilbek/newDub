# Generated by Django 5.0.3 on 2024-10-08 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_short'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.CharField(max_length=300)),
                ('rasm', models.ImageField(upload_to='media/')),
                ('hasib', models.CharField(max_length=400)),
                ('text', models.TextField()),
                ('con', models.CharField(max_length=400)),
            ],
        ),
    ]
