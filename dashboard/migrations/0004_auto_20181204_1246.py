# Generated by Django 2.1.3 on 2018-12-04 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20181202_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollments',
            name='label',
            field=models.CharField(default='-', max_length=15),
        ),
        migrations.AddField(
            model_name='enrollments',
            name='performance',
            field=models.CharField(default='-', max_length=15),
        ),
        migrations.AddField(
            model_name='enrollments',
            name='persistance',
            field=models.CharField(default='-', max_length=15),
        ),
    ]
