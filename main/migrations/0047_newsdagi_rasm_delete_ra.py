# Generated by Django 5.1.2 on 2024-10-13 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0046_newsdagi_categ_delete_categ'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsdagi_rasm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rasm', models.ImageField(upload_to='media/', verbose_name='newsdagi headerdi tagidagi rasmni krting:')),
            ],
        ),
        migrations.DeleteModel(
            name='Ra',
        ),
    ]
