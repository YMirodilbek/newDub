# Generated by Django 5.1.2 on 2024-11-04 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0132_rename_pdf9home_pdf9homes_rename_pdf9_pdf9homes2'),
    ]

    operations = [
        migrations.CreateModel(
            name='PdfBurj9',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('nomi1', models.CharField(max_length=300)),
                ('nomi2', models.CharField(max_length=300)),
                ('nomi3', models.CharField(max_length=300)),
                ('nomi4', models.CharField(max_length=300)),
                ('nomi5', models.CharField(max_length=300)),
                ('nomi6', models.CharField(max_length=300)),
                ('nomi7', models.CharField(max_length=300)),
                ('nomi8', models.CharField(max_length=300)),
                ('nomi9', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='PdfTxt9',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text1', models.TextField()),
                ('text2', models.TextField()),
                ('nomi1', models.CharField(max_length=300)),
                ('text3', models.TextField()),
                ('nomi2', models.CharField(max_length=300)),
                ('nomi3', models.CharField(max_length=300)),
                ('nomi4', models.CharField(max_length=300)),
                ('nomi5', models.CharField(max_length=300)),
                ('nomi6', models.CharField(max_length=300)),
                ('text4', models.TextField()),
                ('text5', models.TextField()),
                ('text6', models.TextField()),
            ],
        ),
    ]
