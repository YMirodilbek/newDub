# Generated by Django 5.1 on 2024-09-06 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi1', models.CharField(max_length=100)),
                ('nomi2', models.CharField(max_length=100)),
                ('yozuv', models.CharField(max_length=100)),
                ('text', models.TextField()),
            ],
        ),
    ]
