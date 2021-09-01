from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect

from .forms import english_news_add, english_news_view, english_news_add_other
from .models import en_news, en_sports, en_main_news, en_interview, en_article, en_editorial, en_latest_news
from app.models import youtubelink


def en_main_page(request):
    today = datetime.now()
    date_time_today = today.strftime('%B %d %Y, %A')

    main_news_all = en_main_news.objects.all().order_by('-id')[0:3]

    latest_news_all_1 = en_latest_news.objects.all().order_by('-date_time_picker')
    en_latest_news_all = []
    for items in latest_news_all_1:
        if str(items.date_time_picker) <= str(today):
            en_latest_news_all.append(items)
    en_latest_news_all = en_latest_news_all[0:6]

    en_editorial_all_1 = en_editorial.objects.all().order_by('-date_time_picker')
    en_editorial_all = []
    for items in en_editorial_all_1:
        if str(items.date_time_picker) <= str(today):
            en_editorial_all.append(items)
    en_editorial_all = en_editorial_all[0:7]

    en_news_1 = en_news.objects.all().order_by('-date_time_picker')
    en_news_all = []
    for items in en_news_1:
        if str(items.date_time_picker) <= str(today):
            en_news_all.append(items)

    en_news_first = en_news_all[0]
    en_news_rest = en_news_all[1:4]

    en_sports_1 = en_sports.objects.all().order_by('-date_time_picker')
    en_sports_all = []
    for items in en_sports_1:
        if str(items.date_time_picker) <= str(today):
            en_sports_all.append(items)

    en_sports_first = en_sports_all[0]
    en_sports_rest = en_sports_all[1:4]

    en_article_all_1 = en_article.objects.all().order_by('-date_time_picker')
    en_article_all = []
    for items in en_article_all_1:
        if str(items.date_time_picker) <= str(today):
            en_article_all.append(items)

    en_article_all = en_article_all[0:3]

    en_interview_all_1 = en_interview.objects.all().order_by('-date_time_picker')
    en_interview_all = []
    for items in en_interview_all_1:
        if str(items.date_time_picker) <= str(today):
            en_interview_all.append(items)

    en_interview_all = en_interview_all[0:3]

    youtubelink_first = youtubelink.objects.last()
    youtubelink_col_1 = youtubelink.objects.all().order_by('-id')[1:3]
    youtubelink_col_2 = youtubelink.objects.all().order_by('-id')[3:5]

    context = {'date_time_today': date_time_today, 'main_news_all': main_news_all,
               'en_editorial_all': en_editorial_all, 'en_news_first': en_news_first,
               'en_news_rest': en_news_rest, 'en_sports_first': en_sports_first,
               'en_sports_rest': en_sports_rest, 'en_article_all': en_article_all,
               'en_interview_all': en_interview_all, 'youtubelink_first': youtubelink_first,
               'youtubelink_col_1': youtubelink_col_1, 'youtubelink_col_2': youtubelink_col_2,
               'en_latest_news_all': en_latest_news_all}

    return render(request, "english/main.html", context)


def all_news(request, news_types):

    today = datetime.now()
    date_time_today = today.strftime('%B %d %Y, %A')

    if news_types == 'article':
        article_news_1 = en_article.objects.all().order_by('-date_time_picker')
        article_news = []

        for items in article_news_1:
            if str(items.date_time_picker) <= str(today):
                article_news.append(items)

        context = {'date_time_today': date_time_today, 'new_objects': article_news, 'news_types': news_types}
        return render(request, "english/all_news.html", context)

    if news_types == 'interview':
        interview_news_1 = en_interview.objects.all().order_by('-date_time_picker')
        interview_news = []

        for items in interview_news_1:
            if str(items.date_time_picker) <= str(today):
                interview_news.append(items)

        context = {'date_time_today': date_time_today, 'new_objects': interview_news, 'news_types': news_types}
        return render(request, "english/all_news.html", context)

    if news_types == 'sports':
        sports_news_1 = en_sports.objects.all().order_by('-date_time_picker')
        sports_news = []

        for items in sports_news_1:
            if str(items.date_time_picker) <= str(today):
                sports_news.append(items)

        context = {'date_time_today': date_time_today, 'new_objects': sports_news, 'news_types': news_types}
        return render(request, "english/all_news.html", context)

    if news_types == 'editorial':
        editorial_news_1 = en_editorial.objects.all().order_by('-date_time_picker')
        editorial_news = []

        for items in editorial_news_1:
            if str(items.date_time_picker) <= str(today):
                editorial_news.append(items)

        context = {'date_time_today': date_time_today, 'new_objects': editorial_news, 'news_types': news_types}
        return render(request, "english/all_news.html", context)


def per_page(request, news_types, dates, news_id):

    today = datetime.now()
    date_time_today = today.strftime('%B %d %Y, %A')

    if news_types == 'main_news':
        news_object = en_main_news.objects.filter(date_uploaded=dates, id=news_id).last()
        context = {'date_time_today': date_time_today, 'news_object': news_object}
        return render(request, "english/per_page.html", context)

    if news_types == 'editorial':
        news_object = en_editorial.objects.filter(date_uploaded=dates, id=news_id).last()
        context = {'date_time_today': date_time_today, 'news_object': news_object}
        return render(request, "english/per_page.html", context)

    if news_types == 'news':
        news_object = en_news.objects.filter(date_uploaded=dates, id=news_id).last()
        context = {'date_time_today': date_time_today, 'news_object': news_object}
        return render(request, "english/per_page.html", context)

    if news_types == 'sports':
        news_object = en_sports.objects.filter(date_uploaded=dates, id=news_id).last()
        context = {'date_time_today': date_time_today, 'news_object': news_object}
        return render(request, "english/per_page.html", context)

    if news_types == 'article':
        news_object = en_article.objects.filter(date_uploaded=dates, id=news_id).last()
        context = {'date_time_today': date_time_today, 'news_object': news_object}
        return render(request, "english/per_page.html", context)

    if news_types == 'interview':
        news_object = en_interview.objects.filter(date_uploaded=dates, id=news_id).last()
        context = {'date_time_today': date_time_today, 'news_object': news_object}
        return render(request, "english/per_page.html", context)


@login_required(login_url='/admin_login/')
def en_admin_home(request):
    current_user = request.user

    main_news_all = en_main_news.objects.all().order_by('-id')
    paginator_en_main_news = Paginator(main_news_all, 10)
    page_number_en_main_news = request.GET.get('page1')
    try:
        page_obj_en_main_news = paginator_en_main_news.page(page_number_en_main_news)
    except PageNotAnInteger:
        page_obj_en_main_news = paginator_en_main_news.page(1)
    except EmptyPage:
        page_obj_en_main_news = paginator_en_main_news.page(paginator_en_main_news.num_pages)

    context = {'current_user': current_user, 'main_news_all': page_obj_en_main_news}

    return render(request, "english/dashboard/index.html", context)


@login_required(login_url='/admin_login/')
def en_national_news(request):

    current_user = request.user

    national_news = en_news.objects.all().order_by('-date_time_picker')
    paginator_en_news = Paginator(national_news, 10)
    page_number_en_news = request.GET.get('page1')
    try:
        page_obj_en_news = paginator_en_news.page(page_number_en_news)
    except PageNotAnInteger:
        page_obj_en_news = paginator_en_news.page(1)
    except EmptyPage:
        page_obj_en_news = paginator_en_news.page(paginator_en_news.num_pages)

    national_sports = en_sports.objects.all().order_by('-date_time_picker')
    paginator_en_sports = Paginator(national_sports, 10)
    page_number_en_sports = request.GET.get('page2')
    try:
        page_obj_en_sports = paginator_en_sports.page(page_number_en_sports)
    except PageNotAnInteger:
        page_obj_en_sports = paginator_en_sports.page(1)
    except EmptyPage:
        page_obj_en_sports = paginator_en_sports.page(paginator_en_sports.num_pages)

    context = {'current_user': current_user, 'national_news': page_obj_en_news,
               'national_sports': page_obj_en_sports}

    return render(request, "english/dashboard/nationaNews.html", context)


@login_required(login_url='/admin_login/')
def en_interview_news(request):

    current_user = request.user

    interview_news = en_interview.objects.all().order_by('-date_time_picker')
    paginator_en_interview = Paginator(interview_news, 10)
    page_number_en_interview = request.GET.get('page')
    try:
        page_obj_en_interview = paginator_en_interview.page(page_number_en_interview)
    except PageNotAnInteger:
        page_obj_en_interview = paginator_en_interview.page(1)
    except EmptyPage:
        page_obj_en_interview = paginator_en_interview.page(paginator_en_interview.num_pages)

    context = {'current_user': current_user, 'interview_all': page_obj_en_interview}
    return render(request, "english/dashboard/Interview_en.html", context)


@login_required(login_url='/admin_login/')
def en_interview_news_add(request, news_types):

    if news_types == 'interview':
        form = english_news_add_other()
        context = {'form': form, 'news_types': news_types}
        return render(request, "english/dashboard/add_news_other_en.html", context)

    if news_types == 'article':
        form = english_news_add_other()
        context = {'form': form, 'news_types': news_types}
        return render(request, "english/dashboard/add_news_other_en.html", context)

    if news_types == 'editorial':
        form = english_news_add_other()
        context = {'form': form, 'news_types': news_types}
        return render(request, "english/dashboard/add_news_other_en.html", context)


@login_required(login_url='/admin_login/')
def en_interview_news_add_post(request, news_types):
    if request.method == 'POST':
        form = english_news_add_other(request.POST, request.FILES)

        if form.is_valid():
            title = form.cleaned_data.get("title")
            editor_name = form.cleaned_data.get("editor_name")
            location = form.cleaned_data.get("location")
            photo_img = form.cleaned_data.get("photo_img")
            news_summary = form.cleaned_data.get("news_summary")
            description = form.cleaned_data.get("description")
            date_time_picker = form.cleaned_data.get("date_time_picker")

            if news_types == 'interview':
                en_news_add = en_interview.objects.create(title=title, editor_name=editor_name, photo_img=photo_img,
                                                          location=location, description=description,
                                                          news_summary=news_summary,
                                                          date_time_picker=date_time_picker)

                en_news_add.save()

                latest_add = en_latest_news.objects.create(title=title, editor_name=editor_name, photo_img=photo_img,
                                                           location=location, description=description,
                                                           news_summary=news_summary, date_time_picker=date_time_picker)
                latest_add.save()

                return redirect('en_interview_news')

            if news_types == 'article':
                en_news_add = en_article.objects.create(title=title, editor_name=editor_name, photo_img=photo_img,
                                                        location=location, description=description,
                                                        news_summary=news_summary,
                                                        date_time_picker=date_time_picker)

                en_news_add.save()

                latest_add = en_latest_news.objects.create(title=title, editor_name=editor_name, photo_img=photo_img,
                                                           location=location, description=description,
                                                           news_summary=news_summary, date_time_picker=date_time_picker)
                latest_add.save()

                return redirect('en_article_news')

            if news_types == 'editorial':
                en_news_add = en_editorial.objects.create(title=title, editor_name=editor_name, photo_img=photo_img,
                                                          location=location, description=description,
                                                          news_summary=news_summary,
                                                          date_time_picker=date_time_picker)

                en_news_add.save()

                latest_add = en_latest_news.objects.create(title=title, editor_name=editor_name, photo_img=photo_img,
                                                           location=location, description=description,
                                                           news_summary=news_summary, date_time_picker=date_time_picker)
                latest_add.save()

                return redirect('en_editorial_news')


@login_required(login_url='/admin_login/')
def en_views_news_other(request, news_types, dates, news_id):

    if news_types == 'interview':
        news_query = en_interview.objects.filter(date_uploaded=dates, id=news_id).last()
        context = {'news_query': news_query}

        return render(request, "english/dashboard/view_news_other_en.html", context)

    if news_types == 'article':
        news_query = en_article.objects.filter(date_uploaded=dates, id=news_id).last()
        context = {'news_query': news_query}

        return render(request, "english/dashboard/view_news_other_en.html", context)

    if news_types == 'editorial':
        news_query = en_editorial.objects.filter(date_uploaded=dates, id=news_id).last()
        context = {'news_query': news_query}

        return render(request, "english/dashboard/view_news_other_en.html", context)


@login_required(login_url='/admin_login/')
def en_edit_news_other(request, news_types, dates, news_id):

    if news_types == 'en_interview':
        news_query = en_interview.objects.get(date_uploaded=dates, id=news_id)
        form = english_news_view(instance=news_query)
        context = {'form': form, 'news_query': news_query}

        return render(request, "english/dashboard/edit_news_other_en.html", context)

    if news_types == 'en_article':
        news_query = en_article.objects.get(date_uploaded=dates, id=news_id)
        form = english_news_view(instance=news_query)
        context = {'form': form, 'news_query': news_query}

        return render(request, "english/dashboard/edit_news_other_en.html", context)

    if news_types == 'en_editorial':
        news_query = en_editorial.objects.get(date_uploaded=dates, id=news_id)
        form = english_news_view(instance=news_query)
        context = {'form': form, 'news_query': news_query}

        return render(request, "english/dashboard/edit_news_other_en.html", context)


@login_required(login_url='/admin_login/')
def en_update_news_other_post(request, news_types, dates, news_id):

    if request.method == 'POST':
        form = english_news_add_other(request.POST, request.FILES)

        if form.is_valid():
            title = form.cleaned_data.get("title")
            editor_name = form.cleaned_data.get("editor_name")
            location = form.cleaned_data.get("location")
            photo_img = form.cleaned_data.get("photo_img")
            news_summary = form.cleaned_data.get("news_summary")
            description = form.cleaned_data.get("description")

            date_time_picker = form.cleaned_data.get("date_time_picker")

            if news_types == 'en_interview':
                news_query = en_interview.objects.get(date_uploaded=dates, id=news_id)

                news_image = news_query.photo_img
                news_image.delete()

                news_query.title = title
                news_query.editor_name = editor_name
                news_query.location = location
                news_query.photo_img = photo_img
                news_query.news_summary = news_summary
                news_query.description = description
                news_query.date_time_picker = date_time_picker
                news_query.save()
                return redirect('en_interview_news')

            if news_types == 'en_article':
                news_query = en_article.objects.get(date_uploaded=dates, id=news_id)

                news_image = news_query.photo_img
                news_image.delete()

                news_query.title = title
                news_query.editor_name = editor_name
                news_query.location = location
                news_query.photo_img = photo_img
                news_query.news_summary = news_summary
                news_query.description = description
                news_query.date_time_picker = date_time_picker
                news_query.save()
                return redirect('en_article_news')

            if news_types == 'en_editorial':
                news_query = en_editorial.objects.get(date_uploaded=dates, id=news_id)

                news_image = news_query.photo_img
                news_image.delete()

                news_query.title = title
                news_query.editor_name = editor_name
                news_query.location = location
                news_query.photo_img = photo_img
                news_query.news_summary = news_summary
                news_query.description = description
                news_query.date_time_picker = date_time_picker
                news_query.save()
                return redirect('en_editorial_news')


@login_required(login_url='/admin_login/')
def en_national_news_view(request, news_types, dates, news_id):

    if news_types == 'News':
        news_query = en_news.objects.filter(date_uploaded=dates, id=news_id).last()
        print(news_query.description)
        context = {'news_query': news_query}

        return render(request, "english/dashboard/view_news_en.html", context)

    if news_types == 'Sports':
        news_query = en_sports.objects.filter(date_uploaded=dates, id=news_id).last()
        print(news_query.description)
        context = {'news_query': news_query}

        return render(request, "english/dashboard/view_news_en.html", context)


@login_required(login_url='/admin_login/')
def en_national_news_edit(request, news_types, dates, news_id):

    if news_types == 'News':
        news_query = en_news.objects.get(date_uploaded=dates, id=news_id)
        form = english_news_view(instance=news_query)
        context = {'form': form, 'news_query': news_query}

        return render(request, "english/dashboard/edit_news_en.html", context)

    if news_types == 'Sports':
        news_query = en_sports.objects.get(date_uploaded=dates, id=news_id)
        form = english_news_view(instance=news_query)
        context = {'form': form, 'news_query': news_query}

        return render(request, "english/dashboard/edit_news_en.html", context)


@login_required(login_url='/admin_login/')
def en_national_news_post(request, news_types, dates, news_id):

    if request.method == 'POST':
        form = english_news_view(request.POST, request.FILES)

        if form.is_valid():
            title = form.cleaned_data.get("title")
            editor_name = form.cleaned_data.get("editor_name")
            location = form.cleaned_data.get("location")
            photo_img = form.cleaned_data.get("photo_img")
            news_summary = form.cleaned_data.get("news_summary")
            description = form.cleaned_data.get("description")

            date_time_picker = form.cleaned_data.get("date_time_picker")

            if news_types == 'en_news':
                news_query = en_news.objects.get(date_uploaded=dates, id=news_id)

                news_image = news_query.photo_img
                news_image.delete()

                news_query.title = title
                news_query.editor_name = editor_name
                news_query.location = location
                news_query.photo_img = photo_img
                news_query.news_summary = news_summary
                news_query.description = description
                news_query.date_time_picker = date_time_picker
                news_query.save()
                return redirect('en_national_news')

            if news_types == 'en_sports':
                news_query = en_sports.objects.get(date_uploaded=dates, id=news_id)

                news_image = news_query.photo_img
                news_image.delete()

                news_query.title = title
                news_query.editor_name = editor_name
                news_query.location = location
                news_query.photo_img = photo_img
                news_query.news_summary = news_summary
                news_query.description = description
                news_query.date_time_picker = date_time_picker
                news_query.save()
                return redirect('en_national_news')


@login_required(login_url='/admin_login/')
def en_main_news_add(request, news_types, dates, news_id):

    if news_types == 'News':
        national_news = en_news.objects.filter(id=news_id, date_uploaded=dates).first()

        main_news = en_main_news(title=national_news.title, editor_name=national_news.editor_name,
                                 location=national_news.location, photo_img=national_news.photo_img,
                                 news_summary=national_news.news_summary,
                                 description=national_news.description)
        main_news.save()
        return redirect('en_admin_home')

    if news_types == 'Sports':
        sports_news = en_sports.objects.filter(id=news_id, date_uploaded=dates).first()

        main_news = en_main_news(title=sports_news.title, editor_name=sports_news.editor_name,
                                 location=sports_news.location, photo_img=sports_news.photo_img,
                                 news_summary=sports_news.news_summary,
                                 description=sports_news.description)
        main_news.save()
        return redirect('en_admin_home')

    if news_types == 'interview':
        interview_news = en_interview.objects.filter(id=news_id, date_uploaded=dates).first()

        main_news = en_main_news(title=interview_news.title, editor_name=interview_news.editor_name,
                                 location=interview_news.location, photo_img=interview_news.photo_img,
                                 news_summary=interview_news.news_summary,
                                 description=interview_news.description)
        main_news.save()
        return redirect('en_admin_home')

    if news_types == 'article':
        article_news = en_article.objects.filter(id=news_id, date_uploaded=dates).first()

        main_news = en_main_news(title=article_news.title, editor_name=article_news.editor_name,
                                 location=article_news.location, photo_img=article_news.photo_img,
                                 news_summary=article_news.news_summary,
                                 description=article_news.description)
        main_news.save()
        return redirect('en_admin_home')

    if news_types == 'editorial':
        editorial_news = en_editorial.objects.filter(id=news_id, date_uploaded=dates).first()

        main_news = en_main_news(title=editorial_news.title, editor_name=editorial_news.editor_name,
                                 location=editorial_news.location, photo_img=editorial_news.photo_img,
                                 news_summary=editorial_news.news_summary,
                                 description=editorial_news.description)
        main_news.save()
        return redirect('en_admin_home')


@login_required(login_url='/admin_login/')
def en_article_news(request):

    current_user = request.user

    article_news = en_article.objects.all().order_by('-date_time_picker')
    paginator_en_article = Paginator(article_news, 10)
    page_number_en_article = request.GET.get('page')
    try:
        page_obj_en_article = paginator_en_article.page(page_number_en_article)
    except PageNotAnInteger:
        page_obj_en_article = paginator_en_article.page(1)
    except EmptyPage:
        page_obj_en_article = paginator_en_article.page(paginator_en_article.num_pages)

    context = {'current_user': current_user, 'article_all': page_obj_en_article}

    return render(request, "english/dashboard/article.html", context)


@login_required(login_url='/admin_login/')
def en_editorial_news(request):

    current_user = request.user

    editorial_news = en_editorial.objects.all().order_by('-date_time_picker')
    paginator_en_editorial = Paginator(editorial_news, 10)
    page_number_en_editorial = request.GET.get('page')
    try:
        page_obj_en_editorial = paginator_en_editorial.page(page_number_en_editorial)
    except PageNotAnInteger:
        page_obj_en_editorial = paginator_en_editorial.page(1)
    except EmptyPage:
        page_obj_en_editorial = paginator_en_editorial.page(paginator_en_editorial.num_pages)

    context = {'current_user': current_user, 'editorial_all': page_obj_en_editorial}

    return render(request, "english/dashboard/Editorial_en.html", context)


@login_required(login_url='/admin_login/')
def en_setting(request):
    admin_all = request.user
    current_user = request.user
    context = {'admin_all': admin_all, 'current_user': current_user}

    return render(request, "english/dashboard/setting.html", context)


@login_required(login_url='/admin_login/')
def en_add_news(request):
    current_user = request.user
    form = english_news_add()
    context = {'current_user': current_user, 'form': form}
    return render(request, "english/dashboard/add_news_en.html", context)


@login_required(login_url='/admin_login/')
def en_add_news_post(request):
    if request.method == 'POST':
        form = english_news_add(request.POST, request.FILES)

        if form.is_valid():
            title = form.cleaned_data.get("title")
            editor_name = form.cleaned_data.get("editor_name")
            location = form.cleaned_data.get("location")
            photo_img = form.cleaned_data.get("photo_img")
            news_summary = form.cleaned_data.get("news_summary")
            description = form.cleaned_data.get("description")
            date_time_picker = form.cleaned_data.get("date_time_picker")
            radio_button = form.cleaned_data.get("radio_button")

            if radio_button == 'News':
                en_news_add = en_news.objects.create(title=title, editor_name=editor_name, photo_img=photo_img,
                                                     location=location, description=description, news_summary=news_summary,
                                                     date_time_picker=date_time_picker)

                en_news_add.save()

                latest_add = en_latest_news.objects.create(title=title, editor_name=editor_name, photo_img=photo_img,
                                                           location=location, description=description,
                                                           news_summary=news_summary, date_time_picker=date_time_picker)
                latest_add.save()

                return redirect('en_national_news')

            if radio_button == 'Sports':
                en_news_add = en_sports.objects.create(title=title, editor_name=editor_name, photo_img=photo_img,
                                                       location=location, description=description, news_summary=news_summary,
                                                       date_time_picker=date_time_picker)

                en_news_add.save()

                latest_add = en_latest_news.objects.create(title=title, editor_name=editor_name, photo_img=photo_img,
                                                           location=location, description=description,
                                                           news_summary=news_summary, date_time_picker=date_time_picker)
                latest_add.save()

                return redirect('en_national_news')



