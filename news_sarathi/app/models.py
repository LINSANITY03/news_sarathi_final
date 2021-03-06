from datetime import datetime
from django.db import models
from django_mysql.models.fields import SizedTextField
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class Profile(models.Model):
    class Meta:
        db_table = 'Profile'
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    contact = models.CharField(max_length=20, default='***')
    authorization = models.CharField(max_length=10, default='All')
    photo_img = models.ImageField(blank=True, null=True, upload_to='photos/admin_user', default=0)
    fullname = models.CharField(max_length=20, default='user')

    def __str__(self):
        return self.user.username


class grihaprista(models.Model):
    class Meta:
        db_table = 'grihaprista'

    title = models.CharField(max_length=200)
    editor_name = models.CharField(max_length=50)
    location = models.CharField(max_length=20)
    photo_img = models.ImageField(blank=True, null=True, upload_to='photos/grihaprista', default=0)
    news_summary = SizedTextField(size_class=2, null=True)
    description = RichTextField(default='enter news')
    date_uploaded = models.DateField(default=datetime.now)
    time_uploaded = models.TimeField(default=datetime.now)
    date_time_picker = models.DateTimeField(default=datetime.now)
    number_of_views = models.BigIntegerField(default=0)
    news_id = models.BigIntegerField(default=0)
    news_type = models.CharField(max_length=20, default='grihaprista')

    def __str__(self):
        return self.title


class Breaking_news(models.Model):
    class Meta:
        db_table = 'Breakin_news'

    title = models.CharField(max_length=200)
    date_uploaded = models.DateField(default=datetime.now)
    time_uploaded = models.TimeField(default=datetime.now)

    def __str__(self):
        return self.title


class Latest_news(models.Model):
    class Meta:
        db_table = 'Latest_news'

    title = models.CharField(max_length=200)
    editor_name = models.CharField(max_length=50)
    location = models.CharField(max_length=20)
    photo_img = models.ImageField(blank=True, null=True, upload_to='photos/Latest_news', default=0)
    news_summary = SizedTextField(size_class=2, null=True)
    description = RichTextField(default='enter news')
    date_uploaded = models.DateField(default=datetime.now)
    time_uploaded = models.TimeField(default=datetime.now)
    date_time_picker = models.DateTimeField(default=datetime.now)
    number_of_views = models.BigIntegerField(default=0)
    news_type = models.CharField(max_length=20, default='latest')

    def __str__(self):
        return self.title


class sandhiya(models.Model):
    class Meta:
        db_table = 'sandhiya'

    title = models.CharField(max_length=200)
    editor_name = models.CharField(max_length=50)
    location = models.CharField(max_length=20)
    photo_img = models.ImageField(blank=True, null=True, upload_to='photos/sandhiya', default=0)
    news_summary = SizedTextField(size_class=2, null=True)
    description = RichTextField(default='enter news')
    date_uploaded = models.DateField(default=datetime.now)
    time_uploaded = models.TimeField(default=datetime.now)
    date_time_picker = models.DateTimeField(default=datetime.now)
    news_type = models.CharField(max_length=20, default='sandhiya')
    number_of_views = models.BigIntegerField(default=0)
    Latest_news = models.OneToOneField(Latest_news, on_delete=models.CASCADE,
                                       related_name="Latest_news_sandhiya", null=True)

    def __str__(self):
        return self.title


class pradesh(models.Model):
    class Meta:
        db_table = 'pradesh'

    title = models.CharField(max_length=200)
    editor_name = models.CharField(max_length=50)
    location = models.CharField(max_length=20)
    photo_img = models.ImageField(blank=True, null=True, upload_to='photos/pradesh', default=0)
    description = RichTextField(default='enter news')
    news_summary = SizedTextField(size_class=2, null=True)
    date_uploaded = models.DateField(default=datetime.now)
    time_uploaded = models.TimeField(default=datetime.now)
    date_time_picker = models.DateTimeField(default=datetime.now)
    news_type = models.CharField(max_length=20, default='pradesh')
    number_of_views = models.BigIntegerField(default=0)
    Latest_news = models.OneToOneField(Latest_news, on_delete=models.CASCADE,
                                       related_name="Latest_news_pradesh", null=True)

    def __str__(self):
        return self.title


class esthaniya(models.Model):
    class Meta:
        db_table = 'esthaniya'

    title = models.CharField(max_length=200)
    editor_name = models.CharField(max_length=50)
    location = models.CharField(max_length=20)
    photo_img = models.ImageField(blank=True, null=True, upload_to='photos/esthaniya', default=0)
    description = RichTextField(default='enter news')
    news_summary = SizedTextField(size_class=2, null=True)
    date_uploaded = models.DateField(default=datetime.now)
    time_uploaded = models.TimeField(default=datetime.now)
    date_time_picker = models.DateTimeField(default=datetime.now)
    news_type = models.CharField(max_length=20, default='esthaniya')
    number_of_views = models.BigIntegerField(default=0)
    Latest_news = models.OneToOneField(Latest_news, on_delete=models.CASCADE,
                                       related_name="Latest_news_esthaniya", null=True)

    def __str__(self):
        return self.title


class manoranjan(models.Model):
    class Meta:
        db_table = 'manoranjan'

    title = models.CharField(max_length=200)
    editor_name = models.CharField(max_length=50)
    location = models.CharField(max_length=20)
    photo_img = models.ImageField(blank=True, null=True, upload_to='photos/manoranjan', default=0)
    news_summary = SizedTextField(size_class=2, null=True)
    description = RichTextField(default='enter news')
    date_uploaded = models.DateField(default=datetime.now)
    time_uploaded = models.TimeField(default=datetime.now)
    date_time_picker = models.DateTimeField(default=datetime.now)
    news_type = models.CharField(max_length=20, default='manoranjan')
    number_of_views = models.BigIntegerField(default=0)
    Latest_news = models.OneToOneField(Latest_news, on_delete=models.CASCADE,
                                       related_name="Latest_news_manoranjan", null=True)

    def __str__(self):
        return self.title


class khelud(models.Model):
    class Meta:
        db_table = 'khelud'

    title = models.CharField(max_length=200)
    editor_name = models.CharField(max_length=50)
    location = models.CharField(max_length=20)
    photo_img = models.ImageField(blank=True, null=True, upload_to='photos/khelud', default=0)
    news_summary = SizedTextField(size_class=2, null=True)
    description = RichTextField(default='enter news')
    date_uploaded = models.DateField(default=datetime.now)
    time_uploaded = models.TimeField(default=datetime.now)
    date_time_picker = models.DateTimeField(default=datetime.now)
    news_type = models.CharField(max_length=20, default='khelud')
    number_of_views = models.BigIntegerField(default=0)
    Latest_news = models.OneToOneField(Latest_news, on_delete=models.CASCADE,
                                       related_name="Latest_news_khelud", null=True)

    def __str__(self):
        return self.title


class antarbarta(models.Model):
    class Meta:
        db_table = 'antarbarta'

    title = models.CharField(max_length=200)
    editor_name = models.CharField(max_length=50)
    location = models.CharField(max_length=20)
    photo_img = models.ImageField(blank=True, null=True, upload_to='photos/antarbarta', default=0)
    news_summary = SizedTextField(size_class=2, null=True)
    description = RichTextField(default='')
    date_uploaded = models.DateField(default=datetime.now)
    time_uploaded = models.TimeField(default=datetime.now)
    date_time_picker = models.DateTimeField(default=datetime.now)
    news_type = models.CharField(max_length=20, default='antarbarta')
    number_of_views = models.BigIntegerField(default=0)
    Latest_news = models.OneToOneField(Latest_news, on_delete=models.CASCADE,
                                       related_name="Latest_news_antarbarta", null=True)

    def __str__(self):
        return self.title


class bichar_lekh(models.Model):
    class Meta:
        db_table = 'bichar_lekh'

    title = models.CharField(max_length=200)
    editor_name = models.CharField(max_length=50)
    location = models.CharField(max_length=20)
    photo_img = models.ImageField(blank=True, null=True, upload_to='photos/bichar_lekh', default=0)
    news_summary = SizedTextField(size_class=2, null=True)
    description = RichTextField(default='')
    date_uploaded = models.DateField(default=datetime.now)
    time_uploaded = models.TimeField(default=datetime.now)
    date_time_picker = models.DateTimeField(default=datetime.now)
    news_type = models.CharField(max_length=20, default='bichar_lekh')
    number_of_views = models.BigIntegerField(default=0)
    Latest_news = models.OneToOneField(Latest_news, on_delete=models.CASCADE,
                                       related_name="Latest_news_bichar_lekh", null=True)

    def __str__(self):
        return self.title


class suchanapraviti(models.Model):
    class Meta:
        db_table = 'suchanapraviti'

    title = models.CharField(max_length=200)
    editor_name = models.CharField(max_length=50)
    location = models.CharField(max_length=20)
    photo_img = models.ImageField(blank=True, null=True, upload_to='photos/suchanapraviti', default=0)
    news_summary = SizedTextField(size_class=2, null=True)
    description = RichTextField(default='')
    date_uploaded = models.DateField(default=datetime.now)
    time_uploaded = models.TimeField(default=datetime.now)
    date_time_picker = models.DateTimeField(default=datetime.now)
    news_type = models.CharField(max_length=20, default='suchanapraviti')
    number_of_views = models.BigIntegerField(default=0)
    Latest_news = models.OneToOneField(Latest_news, on_delete=models.CASCADE,
                                       related_name="Latest_news_suchanapraviti", null=True)

    def __str__(self):
        return self.title


class antarastriya(models.Model):
    class Meta:
        db_table = 'antarastriya'

    title = models.CharField(max_length=200)
    editor_name = models.CharField(max_length=50)
    location = models.CharField(max_length=20)
    photo_img = models.ImageField(blank=True, null=True, upload_to='photos/antarastriya', default=0)
    news_summary = SizedTextField(size_class=2, null=True)
    description = RichTextField(default='')
    date_uploaded = models.DateField(default=datetime.now)
    time_uploaded = models.TimeField(default=datetime.now)
    date_time_picker = models.DateTimeField(default=datetime.now)
    news_type = models.CharField(max_length=20, default='antarastriya')
    number_of_views = models.BigIntegerField(default=0)
    Latest_news = models.OneToOneField(Latest_news, on_delete=models.CASCADE,
                                       related_name="Latest_news_antarastriya", null=True)

    def __str__(self):
        return self.title


class sampadakiya(models.Model):
    class Meta:
        db_table = 'sampadakiya'

    title = models.CharField(max_length=200)
    editor_name = models.CharField(max_length=50)
    location = models.CharField(max_length=20)
    photo_img = models.ImageField(blank=True, null=True, upload_to='photos/sampadakiya', default=0)
    news_summary = SizedTextField(size_class=2, null=True)
    description = RichTextField(default='')
    date_uploaded = models.DateField(default=datetime.now)
    time_uploaded = models.TimeField(default=datetime.now)
    date_time_picker = models.DateTimeField(default=datetime.now)
    news_type = models.CharField(max_length=20, default='sampadakiya')
    number_of_views = models.BigIntegerField(default=0)
    Latest_news = models.OneToOneField(Latest_news, on_delete=models.CASCADE,
                                       related_name="Latest_news_sampadakiya", null=True)

    def __str__(self):
        return self.title


class youtubelink(models.Model):
    class Meta:
        db_table = 'youtubelink'

    title = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    date_uploaded = models.DateField(default=datetime.now)
    time_uploaded = models.TimeField(default=datetime.now)

    def __str__(self):
        return self.title


class news_comment(models.Model):
    class Meta:
        db_table = 'news_comment'

    full_name = models.CharField(max_length=20)
    thoughts = models.CharField(max_length=200)
    url = models.CharField(max_length=200, default=None)
    time_uploaded = models.DateField(default=datetime.now)

    def __str__(self):
        return self.full_name


class about_us(models.Model):
    class Meta:
        db_table = 'about_us'

    title = models.CharField(max_length=20, default=None)
    content = RichTextField()

    def __str__(self):
        return self.title


class ads_table(models.Model):
    class Meta:
        db_table = 'ads_table'

    title = models.CharField(max_length=200)
    ads_num = models.BigIntegerField()
    date_uploaded = models.DateField(default=datetime.now)
    time_uploaded = models.TimeField(default=datetime.now)
    photo_img = models.ImageField(blank=True, null=True, upload_to='photos/ads_table', default=0)

    def __str__(self):
        return self.ads_num
