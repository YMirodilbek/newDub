# Generated by Django 5.1.2 on 2024-11-01 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0097_rename_img_pdfimg8_img1_remove_pdfimg8_img10_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rasm8Pdf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rasm', models.ImageField(upload_to='media/')),
            ],
        ),
    ]
