# Generated by Django 5.1 on 2024-09-06 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='rasm',
            field=models.ImageField(default=1, upload_to='media/'),
            preserve_default=False,
        ),
    ]
