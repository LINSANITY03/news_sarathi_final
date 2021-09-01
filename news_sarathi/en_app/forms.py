from django import forms

from .models import en_news, en_interview


national_news_choice = [('News', 'News'), ('Sports', 'Sports')]


class english_news_add(forms.ModelForm):
    radio_button = forms.ChoiceField(choices=national_news_choice, widget=forms.RadioSelect)

    class Meta:
        model = en_news
        fields = ('title', 'editor_name', 'location', 'photo_img', 'news_summary', 'description',
                  'date_time_picker')


class english_news_view(forms.ModelForm):

    class Meta:
        model = en_news
        fields = ('title', 'editor_name', 'location', 'photo_img', 'news_summary', 'description',
                  'date_time_picker')


class english_news_add_other(forms.ModelForm):

    class Meta:
        model = en_interview
        fields = ('title', 'editor_name', 'location', 'photo_img', 'news_summary', 'description',
                  'date_time_picker')
