# Generated by Django 3.2.6 on 2021-08-19 06:52

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_admin_user_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='about_us',
            name='content',
            field=ckeditor.fields.RichTextField(default='asd'),
        ),
    ]
