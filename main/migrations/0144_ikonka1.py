# Generated by Django 5.1.2 on 2024-11-08 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0143_pdfpast009'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ikonka1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rasm1', models.ImageField(upload_to='media/')),
                ('rasm2', models.ImageField(upload_to='media/')),
            ],
        ),
    ]
