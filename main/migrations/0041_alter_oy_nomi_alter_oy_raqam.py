# Generated by Django 5.1.2 on 2024-10-13 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0040_delete_card1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oy',
            name='nomi',
            field=models.CharField(max_length=200, verbose_name='buttondi nomini krting: '),
        ),
        migrations.AlterField(
            model_name='oy',
            name='raqam',
            field=models.IntegerField(verbose_name='buttondi raqamni krting: '),
        ),
    ]
