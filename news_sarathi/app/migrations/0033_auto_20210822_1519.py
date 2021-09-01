# Generated by Django 3.2.6 on 2021-08-22 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0032_auto_20210821_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='antarastriya',
            name='photo_img',
            field=models.ImageField(blank=True, default='photos/guest-user.jpg', null=True, upload_to='photos/antarastriya'),
        ),
        migrations.AlterField(
            model_name='antarbarta',
            name='photo_img',
            field=models.ImageField(blank=True, default='photos/guest-user.jpg', null=True, upload_to='photos/antarbarta'),
        ),
        migrations.AlterField(
            model_name='bichar_lekh',
            name='photo_img',
            field=models.ImageField(blank=True, default='photos/guest-user.jpg', null=True, upload_to='photos/bichar_lekh'),
        ),
        migrations.AlterField(
            model_name='esthaniya',
            name='photo_img',
            field=models.ImageField(blank=True, default='photos/guest-user.jpg', null=True, upload_to='photos/esthaniya'),
        ),
        migrations.AlterField(
            model_name='grihaprista',
            name='photo_img',
            field=models.ImageField(blank=True, default='photos/guest-user.jpg', null=True, upload_to='photos/grihaprista'),
        ),
        migrations.AlterField(
            model_name='khelud',
            name='photo_img',
            field=models.ImageField(blank=True, default='photos/guest-user.jpg', null=True, upload_to='photos/khelud'),
        ),
        migrations.AlterField(
            model_name='latest_news',
            name='photo_img',
            field=models.ImageField(blank=True, default='photos/guest-user.jpg', null=True, upload_to='photos/Latest_news'),
        ),
        migrations.AlterField(
            model_name='manoranjan',
            name='photo_img',
            field=models.ImageField(blank=True, default='photos/guest-user.jpg', null=True, upload_to='photos/manoranjan'),
        ),
        migrations.AlterField(
            model_name='pradesh',
            name='photo_img',
            field=models.ImageField(blank=True, default='photos/guest-user.jpg', null=True, upload_to='photos/pradesh'),
        ),
        migrations.AlterField(
            model_name='sampadakiya',
            name='photo_img',
            field=models.ImageField(blank=True, default='photos/guest-user.jpg', null=True, upload_to='photos/sampadakiya'),
        ),
        migrations.AlterField(
            model_name='sandhiya',
            name='photo_img',
            field=models.ImageField(blank=True, default='photos/guest-user.jpg', null=True, upload_to='photos/sandhiya'),
        ),
        migrations.AlterField(
            model_name='suchanapraviti',
            name='photo_img',
            field=models.ImageField(blank=True, default='photos/guest-user.jpg', null=True, upload_to='photos/suchanapraviti'),
        ),
    ]