# Generated by Django 5.1 on 2024-09-08 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_contact_qosh'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact_qosh',
            name='email',
        ),
        migrations.RemoveField(
            model_name='contact_qosh',
            name='ism',
        ),
        migrations.RemoveField(
            model_name='contact_qosh',
            name='yosh',
        ),
    ]
