# Generated by Django 5.1.2 on 2024-11-03 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0128_delete_rasm5pdf'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rasm5Pdf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rasm', models.ImageField(upload_to='media/')),
            ],
        ),
    ]
