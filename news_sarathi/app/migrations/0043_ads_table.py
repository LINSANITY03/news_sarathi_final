# Generated by Django 3.2.6 on 2021-08-26 06:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0042_auto_20210826_1106'),
    ]

    operations = [
        migrations.CreateModel(
            name='ads_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('ads_num', models.BigIntegerField()),
                ('date_uploaded', models.DateField(default=datetime.datetime.now)),
                ('time_uploaded', models.TimeField(default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'ads_table',
            },
        ),
    ]
