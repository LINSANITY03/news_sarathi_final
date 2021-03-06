# Generated by Django 3.2.6 on 2021-08-15 08:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20210815_1259'),
    ]

    operations = [
        migrations.AddField(
            model_name='latest_news',
            name='date_uploaded',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='main_news',
            name='date_uploaded',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='latest_news',
            name='time_uploaded',
            field=models.TimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='main_news',
            name='time_uploaded',
            field=models.TimeField(default=datetime.datetime.now),
        ),
    ]
