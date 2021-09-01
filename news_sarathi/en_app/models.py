from django.db import models
from django_mysql.models import SizedTextField
from datetime import datetime
from ckeditor.fields import RichTextField


class en_latest_news(models.Model):
    class Meta:
        db_table = 'en_latest_news'

    title = models.CharField(max_length=200)
    editor_name = models.CharField(max_length=50)
    location = models.CharField(max_length=20)
    photo_img = models.ImageField(upload_to='photos/english/en_latest_news', default='0')
    news_summary = SizedTextField(size_class=2, null=True)
    description = RichTextField(default='')
    date_uploaded = models.DateField(default=datetime.now)
    time_uploaded = models.TimeField(default=datetime.now)
    date_time_picker = models.DateTimeField(default=datetime.now)
    news_type = models.CharField(max_length=20, default='en_latest_news')
    number_of_views = models.BigIntegerField(default=0)


class en_main_news(models.Model):
    class Meta:
        db_table = 'en_main_news'

    title = models.CharField(max_length=200)
    editor_name = models.CharField(max_length=50)
    location = models.CharField(max_length=20)
    photo_img = models.ImageField(upload_to='photos/english/en_main_news', default='0')
    news_summary = SizedTextField(size_class=2, null=True)
    description = RichTextField(default='')
    date_uploaded = models.DateField(default=datetime.now)
    time_uploaded = models.TimeField(default=datetime.now)
    number_of_views = models.BigIntegerField(default=0)


class en_news(models.Model):
    class Meta:
        db_table = 'en_news'

    title = models.CharField(max_length=200)
    editor_name = models.CharField(max_length=50)
    location = models.CharField(max_length=20)
    photo_img = models.ImageField(upload_to='photos/english/en_news', default='0')
    news_summary = SizedTextField(size_class=2, null=True)
    description = RichTextField(default='')
    date_uploaded = models.DateField(default=datetime.now)
    time_uploaded = models.TimeField(default=datetime.now)
    date_time_picker = models.DateTimeField(default=datetime.now)
    news_type = models.CharField(max_length=20, default='en_news')
    number_of_views = models.BigIntegerField(default=0)


class en_sports(models.Model):
    class Meta:
        db_table = 'en_sports'

    title = models.CharField(max_length=200)
    editor_name = models.CharField(max_length=50)
    location = models.CharField(max_length=20)
    photo_img = models.ImageField(upload_to='photos/english/en_sports', default='0')
    news_summary = SizedTextField(size_class=2, null=True)
    description = RichTextField(default='')
    date_uploaded = models.DateField(default=datetime.now)
    time_uploaded = models.TimeField(default=datetime.now)
    date_time_picker = models.DateTimeField(default=datetime.now)
    news_type = models.CharField(max_length=20, default='en_sports')
    number_of_views = models.BigIntegerField(default=0)


class en_interview(models.Model):
    class Meta:
        db_table = 'en_interview'

    title = models.CharField(max_length=200)
    editor_name = models.CharField(max_length=50)
    location = models.CharField(max_length=20)
    photo_img = models.ImageField(upload_to='photos/english/en_interview', default='0')
    news_summary = SizedTextField(size_class=2, null=True)
    description = RichTextField(default='')
    date_uploaded = models.DateField(default=datetime.now)
    time_uploaded = models.TimeField(default=datetime.now)
    date_time_picker = models.DateTimeField(default=datetime.now)
    news_type = models.CharField(max_length=20, default='en_interview')
    number_of_views = models.BigIntegerField(default=0)


class en_article(models.Model):
    class Meta:
        db_table = 'en_article'

    title = models.CharField(max_length=200)
    editor_name = models.CharField(max_length=50)
    location = models.CharField(max_length=20)
    photo_img = models.ImageField(upload_to='photos/english/en_article', default='0')
    news_summary = SizedTextField(size_class=2, null=True)
    description = RichTextField(default='')
    date_uploaded = models.DateField(default=datetime.now)
    time_uploaded = models.TimeField(default=datetime.now)
    date_time_picker = models.DateTimeField(default=datetime.now)
    news_type = models.CharField(max_length=20, default='en_article')
    number_of_views = models.BigIntegerField(default=0)


class en_editorial(models.Model):
    class Meta:
        db_table = 'en_editorial'

    title = models.CharField(max_length=200)
    editor_name = models.CharField(max_length=50)
    location = models.CharField(max_length=20)
    photo_img = models.ImageField(upload_to='photos/english/en_editorial', default='0')
    news_summary = SizedTextField(size_class=2, null=True)
    description = RichTextField(default='')
    date_uploaded = models.DateField(default=datetime.now)
    time_uploaded = models.TimeField(default=datetime.now)
    date_time_picker = models.DateTimeField(default=datetime.now)
    news_type = models.CharField(max_length=20, default='en_editorial')
    number_of_views = models.BigIntegerField(default=0)
