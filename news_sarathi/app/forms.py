from datetime import datetime

from ckeditor.widgets import CKEditorWidget
from django import forms
from django.forms import ModelForm

from .models import User
from .models import about_us, sandhiya, antarbarta


class login_form(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', )


national_news_choice = [('सांघिय', 'सांघिय'), ('पादेश', 'पादेश'), ('स्थानिय', 'स्थानिय'), ('मनोरंजन', 'मनोरंजन'),
                        ('खेलकुद', 'खेलकुद')]


class about_us_post(ModelForm):
    class Meta:
        model = about_us
        fields = '__all__'


class National_form(forms.ModelForm):
    title = forms.CharField(label='TITLE', max_length=200,
                            widget=forms.TextInput(attrs={'placeholder': "Your Title..."}))
    author = forms.CharField(label='AUTHOR NAME', max_length=50,
                             widget=forms.TextInput(attrs={'placeholder': "Author Name..."}))
    location = forms.CharField(label='AUTHOR LOCATION', max_length=20,
                               widget=forms.TextInput(attrs={'placeholder': "Author Location..."}))
    img = forms.ImageField(label='SELECT IMAGE')
    # news_summary = forms.CharField(label='NEWS SUMMARY',
    #                                widget=forms.TextInput(attrs={'placeholder': "Your news summary..."}))
    content = forms.CharField(label='DESCRIPTION', widget=CKEditorWidget())
    scheduler = forms.DateTimeField(initial=datetime.now)
    radio_button = forms.ChoiceField(choices=national_news_choice, widget=forms.RadioSelect)

    class Meta:
        model = sandhiya
        fields = ('news_summary',)


class National_edit_form(forms.ModelForm):
    class Meta:
        model = sandhiya
        fields = ('title', 'editor_name', 'location', 'photo_img', 'news_summary', 'description',)


class add_news(forms.ModelForm):
    title = forms.CharField(label='TITLE', max_length=200,
                            widget=forms.TextInput(attrs={'placeholder': "Your Title..."}))
    author = forms.CharField(label='AUTHOR NAME', max_length=50,
                             widget=forms.TextInput(attrs={'placeholder': "Author Name..."}))
    location = forms.CharField(label='AUTHOR LOCATION', max_length=20,
                               widget=forms.TextInput(attrs={'placeholder': "Author Location..."}))
    img = forms.ImageField(label='SELECT IMAGE')
    content = forms.CharField(label='DESCRIPTION', widget=CKEditorWidget())
    date_time_picker = forms.DateTimeField(label='scheduler(24hr)', initial=datetime.now)

    class Meta:
        model = sandhiya
        fields = ('news_summary',)


class add_news_edit(forms.ModelForm):
    class Meta:
        model = antarbarta
        fields = ('title', 'editor_name', 'location', 'photo_img', 'news_summary', 'description',)
