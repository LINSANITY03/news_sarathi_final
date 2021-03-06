# Generated by Django 3.2.6 on 2021-08-26 05:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0041_auto_20210825_1900'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='antarastriya',
            name='date_picker',
        ),
        migrations.RemoveField(
            model_name='antarastriya',
            name='time_picker',
        ),
        migrations.RemoveField(
            model_name='antarbarta',
            name='date_picker',
        ),
        migrations.RemoveField(
            model_name='antarbarta',
            name='time_picker',
        ),
        migrations.RemoveField(
            model_name='bichar_lekh',
            name='date_picker',
        ),
        migrations.RemoveField(
            model_name='bichar_lekh',
            name='time_picker',
        ),
        migrations.RemoveField(
            model_name='esthaniya',
            name='date_picker',
        ),
        migrations.RemoveField(
            model_name='esthaniya',
            name='time_picker',
        ),
        migrations.RemoveField(
            model_name='khelud',
            name='date_picker',
        ),
        migrations.RemoveField(
            model_name='khelud',
            name='time_picker',
        ),
        migrations.RemoveField(
            model_name='latest_news',
            name='date_picker',
        ),
        migrations.RemoveField(
            model_name='latest_news',
            name='time_picker',
        ),
        migrations.RemoveField(
            model_name='manoranjan',
            name='date_picker',
        ),
        migrations.RemoveField(
            model_name='manoranjan',
            name='time_picker',
        ),
        migrations.RemoveField(
            model_name='pradesh',
            name='date_picker',
        ),
        migrations.RemoveField(
            model_name='pradesh',
            name='time_picker',
        ),
        migrations.RemoveField(
            model_name='sampadakiya',
            name='date_picker',
        ),
        migrations.RemoveField(
            model_name='sampadakiya',
            name='time_picker',
        ),
        migrations.RemoveField(
            model_name='sandhiya',
            name='date_picker',
        ),
        migrations.RemoveField(
            model_name='sandhiya',
            name='time_picker',
        ),
        migrations.RemoveField(
            model_name='suchanapraviti',
            name='date_picker',
        ),
        migrations.RemoveField(
            model_name='suchanapraviti',
            name='time_picker',
        ),
        migrations.AddField(
            model_name='antarastriya',
            name='date_time_picker',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='antarbarta',
            name='date_time_picker',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='bichar_lekh',
            name='date_time_picker',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='esthaniya',
            name='date_time_picker',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='khelud',
            name='date_time_picker',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='latest_news',
            name='date_time_picker',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='manoranjan',
            name='date_time_picker',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='pradesh',
            name='date_time_picker',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='sampadakiya',
            name='date_time_picker',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='sandhiya',
            name='date_time_picker',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='suchanapraviti',
            name='date_time_picker',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
