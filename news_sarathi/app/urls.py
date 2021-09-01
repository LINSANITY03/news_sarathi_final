from django.urls import path
from . import views

urlpatterns = [

    path('', views.main_page, name='main_page'),
    path('all_news/<str:news_types>', views.all_news, name='all_news'),
    path('per_page/<str:news_types>/<str:dates>/<int:news_id>', views.per_page, name='per_page'),

    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_home/', views.admin_home, name='admin_home'),
    path('admin_login_post/', views.admin_login_post, name='admin_login_post'),

    path('admin_add_user/', views.admin_add_user, name='admin_add_user'),
    path('admin_add_user_post/', views.admin_add_user_post, name='admin_add_user_post'),
    path('admin_edit_user/<str:authorization>/<int:admin_id>', views.admin_edit_user, name='admin_edit_user'),
    path('admin_edit_user_post/<str:authorization>/<int:admin_id>', views.admin_edit_user_post, name='admin_edit_user_post'),
    path('admin_user_delete/<str:authorization>/<int:admin_id>', views.admin_user_delete, name='admin_user_delete'),

    path('ads_page/', views.ads_page, name='ads_page'),
    path('ads_page/add_ads/<str:ads_id>', views.add_ads_page, name='add_ads_page'),
    path('add_ads_page_post/<str:ads_id>', views.add_ads_page_post, name='add_ads_page_post'),
    path('ads_page/edit_ads/<str:ads_id>', views.edit_ads_page, name='edit_ads_page'),
    path('del_ads/<str:ads_id>', views.del_ads, name='del_ads'),

    path('admin_add_youtube/', views.admin_add_youtube, name='admin_add_youtube'),
    path('admin_add_youtube_post/', views.admin_add_youtube_post, name='admin_add_youtube_post'),
    path('admin_add_youtube_view/<str:dates>/<int:news_id>', views.admin_add_youtube_view,
         name='admin_add_youtube_view'),
    path('admin_add_youtube_edit/<str:dates>/<int:news_id>', views.admin_add_youtube_edit,
         name='admin_add_youtube_edit'),

    path('admin_add_grihaprista/<str:news_types>/<str:dates>/<int:news_id>', views.admin_add_grihaprista,
         name='admin_add_grihaprista'),

    path('admin_add_breaking_news/', views.admin_add_breaking_news, name='admin_add_breaking_news'),
    path('admin_add_breaking_news_post/', views.admin_add_breaking_news_post, name='admin_add_breaking_news_post'),
    path('admin_add_breaking_news_view/<str:dates>/<int:news_id>', views.admin_add_breaking_news_view,
         name='admin_add_breaking_news_view'),
    path('admin_add_breaking_news_edit/<str:dates>/<int:news_id>', views.admin_add_breaking_news_edit,
         name='admin_add_breaking_news_edit'),
    path('admin_breaking_news_post/<str:dates>/<int:news_id>', views.admin_breaking_news_post,
         name='admin_breaking_news_post'),

    path('admin_add_national_news/', views.admin_add_national_news, name='admin_add_national_news'),
    path('admin_add_national_news_post/', views.admin_add_national_news_post, name='admin_add_national_news_post'),

    path('admin_smsPoll/', views.admin_smsPoll, name='admin_smsPoll'),
    path('admin_pollquestion/', views.admin_pollquestion, name='admin_pollquestion'),
    path('admin_nationaNews/', views.admin_nationaNews, name='admin_nationaNews'),
    path('admin_national_news_view/<str:news_types>/<str:dates>/<int:news_id>', views.admin_national_news_view,
         name='admin_national_news_view'),
    path('admin_national_news_edit/<str:news_types>/<str:dates>/<int:news_id>', views.admin_national_news_edit,
         name='admin_national_news_edit'),
    path('admin_national_news_post/<str:news_types>/<str:dates>/<int:news_id>', views.admin_national_news_post,
         name='admin_national_news_post'),

    path('admin_Interview/', views.admin_Interview, name='admin_Interview'),
    path('admin_add/<str:news_types>', views.admin_add_Interview, name='admin_add_Interview'),
    path('admin_add_post/<str:news_types>', views.admin_add_Interview_post, name='admin_add_Interview_post'),
    path('admin_view/<str:news_types>/<str:dates>/<int:news_id>', views.admin_Interview_view,
         name='admin_Interview_view'),
    path('admin_edit/<str:news_types>/<str:dates>/<int:news_id>', views.admin_Interview_edit,
         name='admin_Interview_edit'),
    path('admin_Interview_post/<str:news_types>/<str:dates>/<int:news_id>', views.admin_Interview_post,
         name='admin_Interview_post'),

    path('admin_delete_news/<str:news_types>/<str:dates>/<int:news_id>', views.admin_delete_news,
         name='admin_delete_news'),

    path('admin_Thoughts/', views.admin_Thoughts, name='admin_Thoughts'),

    path('admin_it_news/', views.admin_it_news, name='admin_it_news'),

    path('admin_InternationalNews/', views.admin_InternationalNews, name='admin_InternationalNews'),

    path('admin_Editorial/', views.admin_Editorial, name='admin_Editorial'),

    path('admin_AboutUs/', views.admin_AboutUs, name='admin_AboutUs'),
    path('admin_AboutUs_edit/', views.admin_AboutUs_edit, name='admin_AboutUs_edit'),
    path('admin_AboutUs_post/', views.admin_AboutUs_post, name='admin_AboutUs_post'),

    path('admin_setting/', views.admin_setting, name='admin_setting'),
    path('admin_profile/', views.admin_profile, name='admin_profile'),
    path('admin_profile_post/<str:authorization>/<int:admin_id>', views.admin_profile_post, name='admin_profile_post'),
    path('ns_setting_1/', views.ns_setting_1, name='ns_setting_1'),
    path('ns_setting_2/', views.ns_setting_2, name='ns_setting_2'),
    path('ns_setting_3/', views.ns_setting_3, name='ns_setting_3'),
    path('ns_setting_4/', views.ns_setting_4, name='ns_setting_4'),

    path('admin_change_password_post/<str:authorization>/<int:admin_id>', views.admin_change_password_post, name='admin_change_password_post'),

    path('logged_out/', views.logged_out, name='logged_out'),

]
