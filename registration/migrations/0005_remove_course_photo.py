# Generated by Django 2.1.3 on 2018-12-08 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_auto_20181208_1956'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='photo',
        ),
    ]
