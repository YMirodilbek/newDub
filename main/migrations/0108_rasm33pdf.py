# Generated by Django 5.1.2 on 2024-11-02 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0107_pdfimg3'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rasm33Pdf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rasm', models.ImageField(upload_to='media/')),
            ],
        ),
    ]
