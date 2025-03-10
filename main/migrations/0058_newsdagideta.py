# Generated by Django 5.1.2 on 2024-10-14 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0057_alter_newsdi_button_nomi1_alter_newsdi_button_nomi2'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsdagiDeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('titlesmal', models.CharField(max_length=200)),
                ('icon', models.ImageField(upload_to='media/')),
                ('rasm', models.ImageField(upload_to='media/')),
                ('nomi', models.CharField(max_length=200)),
                ('nomi1', models.CharField(max_length=200)),
                ('ong1', models.CharField(max_length=200)),
                ('nomi2', models.CharField(max_length=200)),
                ('ong2', models.CharField(max_length=200)),
                ('nomi3', models.CharField(max_length=200)),
                ('button_nomi', models.CharField(max_length=200)),
            ],
        ),
    ]
