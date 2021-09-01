# Generated by Django 3.2.6 on 2021-08-24 09:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0034_auto_20210824_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='antarastriya',
            name='date_picker',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='antarastriya',
            name='time_picker',
            field=models.TimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='antarbarta',
            name='date_picker',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='antarbarta',
            name='time_picker',
            field=models.TimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='bichar_lekh',
            name='date_picker',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='bichar_lekh',
            name='time_picker',
            field=models.TimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='latest_news',
            name='date_picker',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='latest_news',
            name='time_picker',
            field=models.TimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='sampadakiya',
            name='date_picker',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='sampadakiya',
            name='time_picker',
            field=models.TimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='suchanapraviti',
            name='date_picker',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='suchanapraviti',
            name='time_picker',
            field=models.TimeField(default=datetime.datetime.now),
        ),
    ]
