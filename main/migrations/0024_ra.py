# Generated by Django 5.0.3 on 2024-10-08 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_kard'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rasm', models.ImageField(upload_to='media/')),
            ],
        ),
    ]
