# Generated by Django 5.1.2 on 2024-10-31 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0081_pdfimg_img6_pdfimg_img7_pdfimg_img8_pdfimg_img9'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdfimg',
            name='img10',
            field=models.ImageField(default=1, upload_to='media/'),
            preserve_default=False,
        ),
    ]
