# Generated by Django 3.2.6 on 2021-08-12 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210812_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='sandhiya',
            name='news_summary',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='sandhiya',
            name='photo_img',
            field=models.ImageField(blank=True, null=True, upload_to='photos/sandhiya'),
        ),
    ]
