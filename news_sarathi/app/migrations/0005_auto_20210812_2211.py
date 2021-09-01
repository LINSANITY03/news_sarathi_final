# Generated by Django 3.2.6 on 2021-08-12 16:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210812_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='pradesh',
            name='date_uploaded',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='pradesh',
            name='news_summary',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='pradesh',
            name='photo_img',
            field=models.ImageField(blank=True, null=True, upload_to='photos/pradesh'),
        ),
        migrations.AlterField(
            model_name='pradesh',
            name='time_uploaded',
            field=models.TimeField(default=datetime.datetime.now),
        ),
    ]