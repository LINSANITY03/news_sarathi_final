# Generated by Django 3.2.6 on 2021-08-14 06:39

import datetime
from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20210814_1216'),
    ]

    operations = [
        migrations.CreateModel(
            name='sampadakiya',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('editor_name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=20)),
                ('photo_img', models.ImageField(blank=True, null=True, upload_to='photos/sampadakiya')),
                ('news_summary', models.CharField(max_length=300, null=True)),
                ('description', django_mysql.models.SizedTextField(size_class=3)),
                ('date_uploaded', models.DateField(default=datetime.datetime.now)),
                ('time_uploaded', models.TimeField(default=datetime.datetime.now)),
                ('news_type', models.CharField(default='sampadakiya', max_length=20)),
            ],
            options={
                'db_table': 'sampadakiya',
            },
        ),
    ]
