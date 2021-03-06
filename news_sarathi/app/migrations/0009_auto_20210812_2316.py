# Generated by Django 3.2.6 on 2021-08-12 17:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20210812_2248'),
    ]

    operations = [
        migrations.AddField(
            model_name='antarbarta',
            name='date_uploaded',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='antarbarta',
            name='news_summary',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='antarbarta',
            name='news_type',
            field=models.CharField(default='antarbarta', max_length=20),
        ),
        migrations.AlterField(
            model_name='antarbarta',
            name='photo_img',
            field=models.ImageField(blank=True, null=True, upload_to='photos/pradesh'),
        ),
        migrations.AlterField(
            model_name='antarbarta',
            name='time_uploaded',
            field=models.TimeField(default=datetime.datetime.now),
        ),
    ]
