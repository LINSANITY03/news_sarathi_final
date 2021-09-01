# Generated by Django 3.2.6 on 2021-08-14 05:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_bichar_lekh'),
    ]

    operations = [
        migrations.AddField(
            model_name='suchanapraviti',
            name='date_uploaded',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='suchanapraviti',
            name='news_summary',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='suchanapraviti',
            name='news_type',
            field=models.CharField(default='suchanapraviti', max_length=20),
        ),
        migrations.AlterField(
            model_name='suchanapraviti',
            name='photo_img',
            field=models.ImageField(blank=True, null=True, upload_to='photos/suchanapraviti'),
        ),
        migrations.AlterField(
            model_name='suchanapraviti',
            name='time_uploaded',
            field=models.TimeField(default=datetime.datetime.now),
        ),
    ]
