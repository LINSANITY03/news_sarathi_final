# Generated by Django 3.2.6 on 2021-08-31 09:51

import ckeditor.fields
import datetime
from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('en_app', '0004_en_interview'),
    ]

    operations = [
        migrations.CreateModel(
            name='en_article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('editor_name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=20)),
                ('photo_img', models.ImageField(blank=True, default='', null=True, upload_to='photos/english/en_article')),
                ('news_summary', django_mysql.models.SizedTextField(null=True, size_class=2)),
                ('description', ckeditor.fields.RichTextField(default='')),
                ('date_uploaded', models.DateField(default=datetime.datetime.now)),
                ('time_uploaded', models.TimeField(default=datetime.datetime.now)),
                ('date_time_picker', models.DateTimeField(default=datetime.datetime.now)),
                ('news_type', models.CharField(default='en_article', max_length=20)),
                ('number_of_views', models.BigIntegerField(default=0)),
            ],
            options={
                'db_table': 'en_article',
            },
        ),
    ]
