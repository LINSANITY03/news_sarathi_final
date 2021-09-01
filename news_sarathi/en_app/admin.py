from django.contrib import admin
from .models import en_news, en_sports, en_latest_news, en_article, en_interview, en_editorial, en_main_news


admin.site.register(en_news)
admin.site.register(en_sports)
admin.site.register(en_latest_news)
admin.site.register(en_article)
admin.site.register(en_interview)
admin.site.register(en_editorial)
admin.site.register(en_main_news)
