# Generated by Django 3.2.6 on 2021-08-21 03:21

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_auto_20210821_0905'),
    ]

    operations = [
        migrations.AddField(
            model_name='antarastriya',
            name='description',
            field=ckeditor.fields.RichTextField(default=''),
        ),
        migrations.AddField(
            model_name='antarbarta',
            name='description',
            field=ckeditor.fields.RichTextField(default=''),
        ),
        migrations.AddField(
            model_name='bichar_lekh',
            name='description',
            field=ckeditor.fields.RichTextField(default=''),
        ),
        migrations.AddField(
            model_name='sampadakiya',
            name='description',
            field=ckeditor.fields.RichTextField(default=''),
        ),
        migrations.AddField(
            model_name='suchanapraviti',
            name='description',
            field=ckeditor.fields.RichTextField(default=''),
        ),
    ]
