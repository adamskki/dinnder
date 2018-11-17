# Generated by Django 2.1.3 on 2018-11-17 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dinder', '0002_auto_20181117_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='dinderevent',
            name='localization',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='dindergroup',
            name='is_private',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dinderprofile',
            name='image',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='dinderprofile',
            name='localization',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
