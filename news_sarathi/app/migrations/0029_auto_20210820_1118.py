# Generated by Django 3.2.6 on 2021-08-20 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_auto_20210820_1053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grihaprista',
            name='description',
        ),
        migrations.RemoveField(
            model_name='latest_news',
            name='description',
        ),
    ]
