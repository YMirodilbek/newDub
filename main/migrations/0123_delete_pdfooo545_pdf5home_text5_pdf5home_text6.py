# Generated by Django 5.1.2 on 2024-11-03 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0122_rename_pdfhome5e_pdfooo545'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Pdfooo545',
        ),
        migrations.AddField(
            model_name='pdf5home',
            name='text5',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pdf5home',
            name='text6',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
