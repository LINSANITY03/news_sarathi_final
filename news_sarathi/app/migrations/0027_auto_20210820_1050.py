# Generated by Django 3.2.6 on 2021-08-20 05:05

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_about_us_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='esthaniya',
            name='news_summary',
        ),
        migrations.RemoveField(
            model_name='khelud',
            name='description',
        ),
        migrations.RemoveField(
            model_name='manoranjan',
            name='description',
        ),
        migrations.RemoveField(
            model_name='pradesh',
            name='description',
        ),
        migrations.RemoveField(
            model_name='sandhiya',
            name='description',
        ),
        migrations.AlterField(
            model_name='about_us',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
