# Generated by Django 3.2.6 on 2021-09-01 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0050_auto_20210901_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='grihaprista',
            name='news_id',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='grihaprista',
            name='news_type',
            field=models.CharField(default='grihaprista', max_length=20),
        ),
    ]
