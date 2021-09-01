from django.urls import path
from . import views

urlpatterns = [

    path('', views.en_main_page, name='en_main_page'),
    path('all_news/<str:news_types>', views.all_news, name='all_news'),
    path('per_page/<str:news_types>/<str:dates>/<int:news_id>', views.per_page, name='per_page'),

    path('en_admin_home/', views.en_admin_home, name='en_admin_home'),

    path('en_national_news/', views.en_national_news, name='en_national_news'),
    path('en_national_news/en_add_news/', views.en_add_news, name='en_add_news'),
    path('en_add_news_post/', views.en_add_news_post, name='en_add_news_post'),
    path('en_national_news_view/<str:news_types>/<str:dates>/<int:news_id>', views.en_national_news_view,
         name='en_national_news_view'),
    path('en_national_news_edit/<str:news_types>/<str:dates>/<int:news_id>', views.en_national_news_edit,
         name='en_national_news_edit'),
    path('en_national_news_post/<str:news_types>/<str:dates>/<int:news_id>', views.en_national_news_post,
         name='en_national_news_post'),
    path('en_main_news_add/<str:news_types>/<str:dates>/<int:news_id>', views.en_main_news_add,
         name='en_main_news_add'),


    path('en_interview_news/', views.en_interview_news, name='en_interview_news'),
    path('view/<str:news_types>/<str:dates>/<int:news_id>', views.en_views_news_other,
         name='en_views_news_other'),
    path('edit/<str:news_types>/<str:dates>/<int:news_id>', views.en_edit_news_other,
         name='en_edit_news_other'),
    path('en_update_news_other_post/<str:news_types>/<str:dates>/<int:news_id>', views.en_update_news_other_post,
         name='en_update_news_other_post'),
    path('en_interview_news/en_add_news/<str:news_types>', views.en_interview_news_add,
         name='en_interview_news_add'),
    path('en_interview_news_add_post/<str:news_types>', views.en_interview_news_add_post,
         name='en_interview_news_add_post'),

    path('en_article_news/', views.en_article_news, name='en_article_news'),

    path('en_editorial_news/', views.en_editorial_news, name='en_editorial_news'),

    path('en_setting/', views.en_setting, name='en_setting'),



]

