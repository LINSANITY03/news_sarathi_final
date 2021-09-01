from datetime import date, datetime

import adbs
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import redirect
from django.shortcuts import render

from .forms import about_us_post, National_form, National_edit_form, add_news, add_news_edit, login_form
from .models import sandhiya, pradesh, esthaniya, manoranjan, khelud, antarbarta, bichar_lekh, suchanapraviti, \
    antarastriya, sampadakiya, Breaking_news, youtubelink, grihaprista, Latest_news, about_us, ads_table, Profile


@login_required(login_url='/admin_login/')
def logged_out(request):
    logout(request)
    return redirect('/admin_login/')


def date_converter():
    today = date.today()
    en_date = today.strftime("%Y/%m/%d")
    np_list = adbs.ad_to_bs(en_date)
    np_date = np_list['ne']['day'] + ' ' + np_list['ne']['str_month'] + ' ' + np_list['ne']['year'] + ', ' + \
              np_list['ne']['str_day_of_week']

    return np_date


def latest_dates_np(value):
    given_date = value
    np_list = adbs.ad_to_bs(given_date)
    np_date = np_list['ne']['year'] + '/' + np_list['ne']['month'] + '/' + np_list['ne']['day']
    return np_date


def main_page(request):
    np_date = date_converter()

    current_date_time = datetime.now()

    grihaprista_all = grihaprista.objects.all().order_by('-id')[0:3]

    breaking_news_all = Breaking_news.objects.all().order_by('-id')

    sampadakiya_all_1 = sampadakiya.objects.all().order_by('-date_time_picker')
    sampadakiya_all = []
    for items in sampadakiya_all_1:
        if str(items.date_time_picker) <= str(current_date_time):
            sampadakiya_all.append(items)
    sampadakiya_all = sampadakiya_all[0:7]

    sandhiya_all_1 = sandhiya.objects.all().order_by('-date_time_picker')
    sandhiya_all = []
    for items in sandhiya_all_1:
        if str(items.date_time_picker) <= str(current_date_time):
            sandhiya_all.append(items)

    sandhiya_first = sandhiya_all[0]
    sandhiya_first_np = latest_dates_np(sandhiya_first.date_uploaded.strftime("%Y/%m/%d"))
    sandhiya_rest = sandhiya_all[1:4]
    sandhiya_list_latest = [items.date_uploaded.strftime("%Y/%m/%d") for items in sandhiya_rest]
    sandhiya_latest_date = [latest_dates_np(each) for each in sandhiya_list_latest]
    final_sandhiya_date = zip(sandhiya_rest, sandhiya_latest_date)

    esthaniya_all_1 = esthaniya.objects.all().order_by('-date_time_picker')
    esthaniya_all = []
    for items in esthaniya_all_1:
        if str(items.date_time_picker) <= str(current_date_time):
            esthaniya_all.append(items)

    esthaniya_first = esthaniya_all[0]
    esthaniya_first_np = latest_dates_np(esthaniya_first.date_uploaded.strftime("%Y/%m/%d"))
    esthaniya_rest = esthaniya_all[1:4]
    esthaniya_list_latest = [items.date_uploaded.strftime("%Y/%m/%d") for items in esthaniya_rest]
    esthaniya_latest_date = [latest_dates_np(each) for each in esthaniya_list_latest]
    final_esthaniya_date = zip(esthaniya_rest, esthaniya_latest_date)

    khelud_all_1 = khelud.objects.all().order_by('-date_time_picker')
    khelud_all = []
    for items in khelud_all_1:
        if str(items.date_time_picker) <= str(current_date_time):
            khelud_all.append(items)

    khelud_first = khelud_all[0]
    khelud_first_np = latest_dates_np(khelud_first.date_uploaded.strftime("%Y/%m/%d"))
    khelud_rest = khelud_all[1:4]
    khelud_list_latest = [items.date_uploaded.strftime("%Y/%m/%d") for items in khelud_rest]
    khelud_latest_date = [latest_dates_np(each) for each in khelud_list_latest]
    final_khelud_date = zip(khelud_rest, khelud_latest_date)

    antarbarta_all_1 = antarbarta.objects.all().order_by('-date_time_picker')
    antarbarta_all = []
    for items in antarbarta_all_1:
        if str(items.date_time_picker) <= str(current_date_time):
            antarbarta_all.append(items)
    antarbarta_all = antarbarta_all[0:2]

    suchanapraviti_all_1 = suchanapraviti.objects.all().order_by('-date_time_picker')
    suchanapraviti_all = []
    for items in suchanapraviti_all_1:
        if str(items.date_time_picker) <= str(current_date_time):
            suchanapraviti_all.append(items)

    suchanapraviti_all = suchanapraviti_all[0:3]
    suchanapraviti_list_latest = [items.date_uploaded.strftime("%Y/%m/%d") for items in suchanapraviti_all]
    suchanapraviti_latest_date = [latest_dates_np(each) for each in suchanapraviti_list_latest]
    final_suchanapraviti_date = zip(suchanapraviti_all, suchanapraviti_latest_date)

    antarastriya_all_1 = antarastriya.objects.all().order_by('-date_time_picker')
    antarastriya_all = []
    for items in antarastriya_all_1:
        if str(items.date_time_picker) <= str(current_date_time):
            antarastriya_all.append(items)

    antarastriya_all = antarastriya_all[0:3]
    antarastriya_list_latest = [items.date_uploaded.strftime("%Y/%m/%d") for items in antarastriya_all]
    antarastriya_latest_date = [latest_dates_np(each) for each in antarastriya_list_latest]
    final_antarastriya_date = zip(antarastriya_all, antarastriya_latest_date)

    youtubelink_first = youtubelink.objects.last()
    youtubelink_col_1 = youtubelink.objects.all().order_by('-id')[1:3]
    youtubelink_col_2 = youtubelink.objects.all().order_by('-id')[3:5]

    latest_news_all_1 = Latest_news.objects.all().order_by('-date_time_picker')
    latest_news_all = []
    for items in latest_news_all_1:
        if str(items.date_time_picker) <= str(current_date_time):
            latest_news_all.append(items)

    latest_news_all = latest_news_all[0:6]

    list_latest = [items.date_uploaded.strftime("%Y/%m/%d") for items in latest_news_all]
    nepali_latest_date = [latest_dates_np(each) for each in list_latest]
    final_date = zip(latest_news_all, nepali_latest_date)

    context = {'grihaprista_all': grihaprista_all, 'breaking_news_all': breaking_news_all,
               'sampadakiya_all': sampadakiya_all, 'sandhiya_first': sandhiya_first,
               'sandhiya_first_np': sandhiya_first_np, 'final_sandhiya_date': final_sandhiya_date,
               'esthaniya_first_np': esthaniya_first_np, 'final_esthaniya_date': final_esthaniya_date,
               'esthaniya_first': esthaniya_first, 'khelud_first': khelud_first,
               'khelud_first_np': khelud_first_np, 'final_khelud_date': final_khelud_date,
               'antarbarta_all': antarbarta_all,
               'final_suchanapraviti_date': final_suchanapraviti_date,
               'final_antarastriya_date': final_antarastriya_date,
               'youtubelink_first': youtubelink_first, 'youtubelink_col_1': youtubelink_col_1,
               'youtubelink_col_2': youtubelink_col_2, 'np_date': np_date,
               'nepali_latest_date': nepali_latest_date, 'final_date': final_date}
    return render(request, 'client/main.html', context)


def all_news(request, news_types):
    current_date_time = datetime.now()

    if news_types == 'sampadakiya':
        sampadakiya_news_1 = sampadakiya.objects.all().order_by('-date_time_picker')
        sampadakiya_news = []

        for items in sampadakiya_news_1:
            if str(items.date_time_picker) <= str(current_date_time):
                sampadakiya_news.append(items)

        breaking_news_all = Breaking_news.objects.all().order_by('-id')

        np_date = date_converter()

        context = {'new_objects': sampadakiya_news, 'breaking_news_all': breaking_news_all, 'np_date': np_date}
        return render(request, 'client/all_news.html', context)

    if news_types == 'sandhiya':
        sandhiya_news_1 = sandhiya.objects.all().order_by('-date_time_picker')
        sandhiya_news = []

        for items in sandhiya_news_1:
            if str(items.date_time_picker) <= str(current_date_time):
                sandhiya_news.append(items)

        breaking_news_all = Breaking_news.objects.all().order_by('-id')

        np_date = date_converter()

        context = {'new_objects': sandhiya_news, 'breaking_news_all': breaking_news_all, 'np_date': np_date}
        return render(request, 'client/all_news.html', context)

    if news_types == 'pradesh':
        pradesh_news_1 = pradesh.objects.all().order_by('-date_time_picker')
        pradesh_news = []

        for items in pradesh_news_1:
            if str(items.date_time_picker) <= str(current_date_time):
                pradesh_news.append(items)

        breaking_news_all = Breaking_news.objects.all().order_by('-id')

        np_date = date_converter()

        context = {'new_objects': pradesh_news, 'breaking_news_all': breaking_news_all, 'np_date': np_date}
        return render(request, 'client/all_news.html', context)

    if news_types == 'esthaniya':
        esthaniya_news_1 = esthaniya.objects.all().order_by('-date_time_picker')
        esthaniya_news = []

        for items in esthaniya_news_1:
            if str(items.date_time_picker) <= str(current_date_time):
                esthaniya_news.append(items)

        breaking_news_all = Breaking_news.objects.all().order_by('-id')

        np_date = date_converter()

        context = {'new_objects': esthaniya_news, 'breaking_news_all': breaking_news_all, 'np_date': np_date}
        return render(request, 'client/all_news.html', context)

    if news_types == 'manoranjan':
        manoranjan_news_1 = manoranjan.objects.all().order_by('-date_time_picker')
        manoranjan_news = []

        for items in manoranjan_news_1:
            if str(items.date_time_picker) <= str(current_date_time):
                manoranjan_news.append(items)

        breaking_news_all = Breaking_news.objects.all().order_by('-id')

        np_date = date_converter()

        context = {'new_objects': manoranjan_news, 'breaking_news_all': breaking_news_all, 'np_date': np_date}
        return render(request, 'client/all_news.html', context)

    if news_types == 'khelud':
        khelud_news_1 = khelud.objects.all().order_by('-date_time_picker')
        khelud_news = []

        for items in khelud_news_1:
            if str(items.date_time_picker) <= str(current_date_time):
                khelud_news.append(items)

        breaking_news_all = Breaking_news.objects.all().order_by('-id')

        np_date = date_converter()

        context = {'new_objects': khelud_news, 'breaking_news_all': breaking_news_all, 'np_date': np_date}
        return render(request, 'client/all_news.html', context)

    if news_types == 'antarbarta':
        antarbarta_news_1 = antarbarta.objects.all().order_by('-date_time_picker')
        antarbarta_news = []

        for items in antarbarta_news_1:
            if str(items.date_time_picker) <= str(current_date_time):
                antarbarta_news.append(items)

        breaking_news_all = Breaking_news.objects.all().order_by('-id')

        np_date = date_converter()

        context = {'new_objects': antarbarta_news, 'breaking_news_all': breaking_news_all, 'np_date': np_date}
        return render(request, 'client/all_news.html', context)

    if news_types == 'bichar_lekh':
        bichar_lekh_news_1 = bichar_lekh.objects.all().order_by('-date_time_picker')
        bichar_lekh_news = []

        for items in bichar_lekh_news_1:
            if str(items.date_time_picker) <= str(current_date_time):
                bichar_lekh_news.append(items)

        breaking_news_all = Breaking_news.objects.all().order_by('-id')

        np_date = date_converter()

        context = {'new_objects': bichar_lekh_news, 'breaking_news_all': breaking_news_all, 'np_date': np_date}
        return render(request, 'client/all_news.html', context)

    if news_types == 'suchanapraviti':
        suchanapraviti_news_1 = suchanapraviti.objects.all().order_by('-date_time_picker')
        suchanapraviti_news = []

        for items in suchanapraviti_news_1:
            if str(items.date_time_picker) <= str(current_date_time):
                suchanapraviti_news.append(items)

        breaking_news_all = Breaking_news.objects.all().order_by('-id')

        np_date = date_converter()

        context = {'new_objects': suchanapraviti_news, 'breaking_news_all': breaking_news_all, 'np_date': np_date}
        return render(request, 'client/all_news.html', context)

    if news_types == 'antarastriya':
        antarastriya_news_1 = antarastriya.objects.all().order_by('-date_time_picker')
        antarastriya_news = []

        for items in antarastriya_news_1:
            if str(items.date_time_picker) <= str(current_date_time):
                antarastriya_news.append(items)

        breaking_news_all = Breaking_news.objects.all().order_by('-id')

        np_date = date_converter()

        context = {'new_objects': antarastriya_news, 'breaking_news_all': breaking_news_all, 'np_date': np_date}
        return render(request, 'client/all_news.html', context)


def per_page(request, news_types, dates, news_id):
    if news_types == 'grihaprista':
        grihaprista_news = grihaprista.objects.filter(date_uploaded=dates, id=news_id).first()

        counter = grihaprista_news.number_of_views + 1
        grihaprista.objects.filter(date_uploaded=dates, id=news_id).update(number_of_views=counter)

        breaking_news_all = Breaking_news.objects.all().order_by('-id')

        np_date = date_converter()

        context = {'new_objects': grihaprista_news, 'breaking_news_all': breaking_news_all, 'np_date': np_date}
        return render(request, 'client/per_page.html', context)

    if news_types == 'Latestnews':
        latest_news = Latest_news.objects.filter(date_uploaded=dates, id=news_id).first()

        counter = latest_news.number_of_views + 1
        Latest_news.objects.filter(date_uploaded=dates, id=news_id).update(number_of_views=counter)

        breaking_news_all = Breaking_news.objects.all().order_by('-id')

        np_date = date_converter()

        context = {'new_objects': latest_news, 'breaking_news_all': breaking_news_all, 'np_date': np_date}
        return render(request, 'client/per_page.html', context)

    if news_types == 'sampadakiya':
        sampadakiya_news = sampadakiya.objects.filter(date_uploaded=dates, id=news_id).first()

        counter = sampadakiya_news.number_of_views + 1
        sampadakiya.objects.filter(date_uploaded=dates, id=news_id).update(number_of_views=counter)

        breaking_news_all = Breaking_news.objects.all().order_by('-id')

        np_date = date_converter()

        context = {'new_objects': sampadakiya_news, 'breaking_news_all': breaking_news_all, 'np_date': np_date}
        return render(request, 'client/per_page.html', context)

    if news_types == 'sandhiya':
        sandhiya_news = sandhiya.objects.filter(date_uploaded=dates, id=news_id).first()

        counter = sandhiya_news.number_of_views + 1
        sandhiya.objects.filter(date_uploaded=dates, id=news_id).update(number_of_views=counter)

        breaking_news_all = Breaking_news.objects.all().order_by('-id')

        np_date = date_converter()

        context = {'new_objects': sandhiya_news, 'breaking_news_all': breaking_news_all, 'np_date': np_date}
        return render(request, 'client/per_page.html', context)

    if news_types == 'pradesh':
        pradesh_news = pradesh.objects.filter(date_uploaded=dates, id=news_id).first()

        counter = pradesh_news.number_of_views + 1
        pradesh.objects.filter(date_uploaded=dates, id=news_id).update(number_of_views=counter)

        breaking_news_all = Breaking_news.objects.all().order_by('-id')

        np_date = date_converter()

        context = {'new_objects': pradesh_news, 'breaking_news_all': breaking_news_all, 'np_date': np_date}
        return render(request, 'client/per_page.html', context)

    if news_types == 'esthaniya':
        esthaniya_news = esthaniya.objects.filter(date_uploaded=dates, id=news_id).first()

        counter = esthaniya_news.number_of_views + 1
        esthaniya.objects.filter(date_uploaded=dates, id=news_id).update(number_of_views=counter)

        breaking_news_all = Breaking_news.objects.all().order_by('-id')

        np_date = date_converter()

        context = {'new_objects': esthaniya_news, 'breaking_news_all': breaking_news_all, 'np_date': np_date}
        return render(request, 'client/per_page.html', context)

    if news_types == 'manoranjan':
        manoranjan_news = manoranjan.objects.filter(date_uploaded=dates, id=news_id).first()

        counter = manoranjan_news.number_of_views + 1
        manoranjan.objects.filter(date_uploaded=dates, id=news_id).update(number_of_views=counter)

        breaking_news_all = Breaking_news.objects.all().order_by('-id')

        np_date = date_converter()

        context = {'new_objects': manoranjan_news, 'breaking_news_all': breaking_news_all, 'np_date': np_date}
        return render(request, 'client/per_page.html', context)

    if news_types == 'khelud':
        khelud_news = khelud.objects.filter(date_uploaded=dates, id=news_id).first()

        counter = khelud_news.number_of_views + 1
        khelud.objects.filter(date_uploaded=dates, id=news_id).update(number_of_views=counter)

        breaking_news_all = Breaking_news.objects.all().order_by('-id')

        np_date = date_converter()

        context = {'new_objects': khelud_news, 'breaking_news_all': breaking_news_all, 'np_date': np_date}
        return render(request, 'client/per_page.html', context)

    if news_types == 'antarbarta':
        antarbarta_news = antarbarta.objects.filter(date_uploaded=dates, id=news_id).first()

        counter = antarbarta_news.number_of_views + 1
        antarbarta.objects.filter(date_uploaded=dates, id=news_id).update(number_of_views=counter)

        breaking_news_all = Breaking_news.objects.all().order_by('-id')

        np_date = date_converter()

        context = {'new_objects': antarbarta_news, 'breaking_news_all': breaking_news_all, 'np_date': np_date}
        return render(request, 'client/per_page.html', context)

    if news_types == 'bichar_lekh':
        bichar_lekh_news = bichar_lekh.objects.filter(date_uploaded=dates, id=news_id).first()

        counter = bichar_lekh_news.number_of_views + 1
        bichar_lekh.objects.filter(date_uploaded=dates, id=news_id).update(number_of_views=counter)

        breaking_news_all = Breaking_news.objects.all().order_by('-id')

        np_date = date_converter()

        context = {'new_objects': bichar_lekh_news, 'breaking_news_all': breaking_news_all, 'np_date': np_date}
        return render(request, 'client/per_page.html', context)

    if news_types == 'suchanapraviti':
        suchanapraviti_news = suchanapraviti.objects.filter(date_uploaded=dates, id=news_id).first()

        counter = suchanapraviti_news.number_of_views + 1
        suchanapraviti.objects.filter(date_uploaded=dates, id=news_id).update(number_of_views=counter)

        breaking_news_all = Breaking_news.objects.all().order_by('-id')

        np_date = date_converter()

        context = {'new_objects': suchanapraviti_news, 'breaking_news_all': breaking_news_all, 'np_date': np_date}
        return render(request, 'client/per_page.html', context)

    if news_types == 'antarastriya':
        antarastriya_news = antarastriya.objects.filter(date_uploaded=dates, id=news_id).first()

        counter = antarastriya_news.number_of_views + 1
        antarastriya.objects.filter(date_uploaded=dates, id=news_id).update(number_of_views=counter)

        breaking_news_all = Breaking_news.objects.all().order_by('-id')

        np_date = date_converter()

        context = {'new_objects': antarastriya_news, 'breaking_news_all': breaking_news_all, 'np_date': np_date}
        return render(request, 'client/per_page.html', context)


@login_required(login_url='/admin_login/')
def admin_home(request):
    current_user = request.user


    breaking_news_all = Breaking_news.objects.all().order_by('-id')
    paginator_breaking_news = Paginator(breaking_news_all, 10)
    page_number_breaking_news = request.GET.get('page_breaking_news_all')
    try:
        page_obj_breaking_news = paginator_breaking_news.page(page_number_breaking_news)
    except PageNotAnInteger:
        page_obj_breaking_news = paginator_breaking_news.page(1)
    except EmptyPage:
        page_obj_breaking_news = paginator_breaking_news.page(paginator_breaking_news.num_pages)

    youtubelink_news_all = youtubelink.objects.all().order_by('-id')
    paginator_youtubelink_news = Paginator(youtubelink_news_all, 10)
    page_number_youtubelink_news = request.GET.get('page_youtubelink_news_all')
    try:
        page_obj_youtubelink_news = paginator_youtubelink_news.page(page_number_youtubelink_news)
    except PageNotAnInteger:
        page_obj_youtubelink_news = paginator_youtubelink_news.page(1)
    except EmptyPage:
        page_obj_youtubelink_news = paginator_youtubelink_news.page(paginator_youtubelink_news.num_pages)

    grihaprista_all = grihaprista.objects.all().order_by('-id')
    paginator_grihaprista = Paginator(grihaprista_all, 10)
    page_number_grihaprista = request.GET.get('page_main_news_all')
    try:
        page_obj_grihaprista = paginator_grihaprista.page(page_number_grihaprista)
    except PageNotAnInteger:
        page_obj_grihaprista = paginator_grihaprista.page(1)
    except EmptyPage:
        page_obj_grihaprista = paginator_grihaprista.page(paginator_grihaprista.num_pages)

    latest_news_all = Latest_news.objects.all().order_by('-id')
    paginator_latest_news = Paginator(latest_news_all, 10)
    page_number_latest_news = request.GET.get('page_latest_news_all')
    try:
        page_obj_latest_news = paginator_latest_news.page(page_number_latest_news)
    except PageNotAnInteger:
        page_obj_latest_news = paginator_latest_news.page(1)
    except EmptyPage:
        page_obj_latest_news = paginator_latest_news.page(paginator_latest_news.num_pages)

    context = {'breaking_news_all': page_obj_breaking_news, 'youtubelink_news_all': page_obj_youtubelink_news,
               'main_news_all': page_obj_grihaprista, 'latest_news_all': page_obj_latest_news,
               'current_user': current_user}
    return render(request, "admin_temp/index.html", context)


@login_required(login_url='/admin_login/')
def admin_add_user(request):
    current_user = request.user

    context = {'current_user': current_user}
    return render(request, 'admin_temp/add_admin_user.html', context)


@login_required(login_url='/admin_login/')
def admin_add_user_post(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        fullname = request.POST['fullname']
        email = request.POST['email']
        contact = request.POST['contact']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        permission = request.POST['permission']

        username_check = User.objects.filter(username=user_name)

        if username_check:

            messages.warning(request, 'username is already taken!')
            return redirect('/admin_add_user/')
        else:
            if password != cpassword:

                messages.warning(request, 'password does not match!')
                return redirect('/admin_add_user/')
            else:

                add_user = User(email=email, username=user_name)
                add_user.set_password(password)
                add_user.save()

                Profile.objects.create(user=add_user, fullname=fullname, contact=contact, authorization=permission)

                messages.success(request, 'User Added!')
                return redirect('/admin_setting/')


@login_required(login_url='/admin_login/')
def admin_edit_user(request, authorization, admin_id):

    current_user = request.user

    user_details = Profile.objects.get(user_id=admin_id, authorization=authorization)
    context = {'user_details': user_details, 'current_user': current_user}
    return render(request, 'admin_temp/edit_admin_user.html', context)


@login_required(login_url='/admin_login/')
def admin_edit_user_post(request, authorization, admin_id):

    if request.method == 'POST':
        user_name = request.POST['user_name']
        current_user_name = request.POST['current_user_name']
        fullname = request.POST['fullname']
        email = request.POST['email']
        contact = request.POST['contact']
        permission = request.POST['permission']

        username_check = User.objects.filter(username=user_name)

        if user_name != current_user_name:
            if username_check:

                messages.warning(request, 'username is already taken!')
                url = '/admin_edit_user/' + authorization + '/' + str(admin_id)
                return redirect(url)
            else:
                user_query = User.objects.get(id=admin_id)

                if user_query:
                    if user_query.profile.authorization == authorization:
                        user_query.user_name = user_name
                        user_query.fullname = fullname
                        user_query.email = email
                        user_query.contact = contact
                        user_query.permission = permission
                        user_query.save()
                        messages.success(request, 'User Updated!')
                        return redirect('/admin_setting/')
                else:
                    messages.error(request, 'no such record found')
                    return redirect('/admin_setting/')
        else:
            user_query = User.objects.get(id=admin_id)
            if user_query:
                user_query.user_name = user_name
                user_query.fullname = fullname
                user_query.email = email
                user_query.contact = contact
                user_query.permission = permission
                user_query.save()
                messages.success(request, 'User Updated!')
                return redirect('/admin_setting/')
            else:
                messages.error(request, 'no such record found')
                return redirect('/admin_setting/')


@login_required(login_url='/admin_login/')
def admin_user_delete(request, authorization, admin_id):
    del_user = User.objects.get(id=admin_id)
    if del_user.profile.authorization == authorization:
        del_user.delete()
        messages.success(request, 'User Deleted')
        return redirect('/admin_setting/')


@login_required(login_url='/admin_login/')
def admin_add_grihaprista(request, news_types, dates, news_id):
    if news_types == 'sandhiya':
        sandhiya_news = sandhiya.objects.filter(id=news_id, date_uploaded=dates).first()

        grihaprista_news = grihaprista(title=sandhiya_news.title, editor_name=sandhiya_news.editor_name,
                                       location=sandhiya_news.location, photo_img=sandhiya_news.photo_img,
                                       news_summary=sandhiya_news.news_summary, description=sandhiya_news.description)
        grihaprista_news.save()
        return redirect('/admin_home/')

    if news_types == 'pradesh':
        pradesh_news = pradesh.objects.filter(id=news_id, date_uploaded=dates).first()

        grihaprista_news = grihaprista(title=pradesh_news.title, editor_name=pradesh_news.editor_name,
                                       location=pradesh_news.location, photo_img=pradesh_news.photo_img,
                                       news_summary=pradesh_news.news_summary, description=pradesh_news.description)
        grihaprista_news.save()
        return redirect('/admin_home/')

    if news_types == 'esthaniya':
        esthaniya_news = esthaniya.objects.filter(id=news_id, date_uploaded=dates).first()

        grihaprista_news = grihaprista(title=esthaniya_news.title, editor_name=esthaniya_news.editor_name,
                                       location=esthaniya_news.location, photo_img=esthaniya_news.photo_img,
                                       news_summary=esthaniya_news.news_summary, description=esthaniya_news.description)
        grihaprista_news.save()
        return redirect('/admin_home/')

    if news_types == 'manoranjan':
        manoranjan_news = manoranjan.objects.filter(id=news_id, date_uploaded=dates).first()

        grihaprista_news = grihaprista(title=manoranjan_news.title, editor_name=manoranjan_news.editor_name,
                                       location=manoranjan_news.location, photo_img=manoranjan_news.photo_img,
                                       news_summary=manoranjan_news.news_summary,
                                       description=manoranjan_news.description)
        grihaprista_news.save()
        return redirect('/admin_home/')

    if news_types == 'pradesh':
        pradesh_news = pradesh.objects.filter(id=news_id, date_uploaded=dates).first()

        grihaprista_news = grihaprista(title=pradesh_news.title, editor_name=pradesh_news.editor_name,
                                       location=pradesh_news.location, photo_img=pradesh_news.photo_img,
                                       news_summary=pradesh_news.news_summary, description=pradesh_news.description)
        grihaprista_news.save()
        return redirect('/admin_home/')

    if news_types == 'khelud':
        khelud_news = khelud.objects.filter(id=news_id, date_uploaded=dates).first()

        grihaprista_news = grihaprista(title=khelud_news.title, editor_name=khelud_news.editor_name,
                                       location=khelud_news.location, photo_img=khelud_news.photo_img,
                                       news_summary=khelud_news.news_summary, description=khelud_news.description)
        grihaprista_news.save()
        return redirect('/admin_home/')

    if news_types == 'antarbarta':
        antarbarta_news = antarbarta.objects.filter(id=news_id, date_uploaded=dates).first()

        grihaprista_news = grihaprista(title=antarbarta_news.title, editor_name=antarbarta_news.editor_name,
                                       location=antarbarta_news.location, photo_img=antarbarta_news.photo_img,
                                       news_summary=antarbarta_news.news_summary,
                                       description=antarbarta_news.description)
        grihaprista_news.save()
        return redirect('/admin_home/')

    if news_types == 'sampadakiya':
        sampadakiya_news = sampadakiya.objects.filter(id=news_id, date_uploaded=dates).first()

        grihaprista_news = grihaprista(title=sampadakiya_news.title, editor_name=sampadakiya_news.editor_name,
                                       location=sampadakiya_news.location, photo_img=sampadakiya_news.photo_img,
                                       news_summary=sampadakiya_news.news_summary,
                                       description=sampadakiya_news.description)
        grihaprista_news.save()
        return redirect('/admin_home/')

    if news_types == 'bichar_lekh':
        bichar_lekh_news = bichar_lekh.objects.filter(id=news_id, date_uploaded=dates).first()

        grihaprista_news = grihaprista(title=bichar_lekh_news.title, editor_name=bichar_lekh_news.editor_name,
                                       location=bichar_lekh_news.location, photo_img=bichar_lekh_news.photo_img,
                                       news_summary=bichar_lekh_news.news_summary,
                                       description=bichar_lekh_news.description)
        grihaprista_news.save()
        return redirect('/admin_home/')

    if news_types == 'suchanapraviti':
        suchanapraviti_news = suchanapraviti.objects.filter(id=news_id, date_uploaded=dates).first()

        grihaprista_news = grihaprista(title=suchanapraviti_news.title, editor_name=suchanapraviti_news.editor_name,
                                       location=suchanapraviti_news.location, photo_img=suchanapraviti_news.photo_img,
                                       news_summary=suchanapraviti_news.news_summary,
                                       description=suchanapraviti_news.description)
        grihaprista_news.save()
        return redirect('/admin_home/')

    if news_types == 'antarastriya':
        antarastriya_news = antarastriya.objects.filter(id=news_id, date_uploaded=dates).first()

        grihaprista_news = grihaprista(title=antarastriya_news.title, editor_name=antarastriya_news.editor_name,
                                       location=antarastriya_news.location, photo_img=antarastriya_news.photo_img,
                                       news_summary=antarastriya_news.news_summary,
                                       description=antarastriya_news.description)
        grihaprista_news.save()
        return redirect('/admin_home/')


@login_required(login_url='/admin_login/')
def admin_add_youtube(request):
    current_user = request.user

    context = {'current_user': current_user}
    return render(request, "admin_temp/add_youtube_link.html", context)


@login_required(login_url='/admin_login/')
def admin_add_youtube_post(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        link = request.POST.get("link")
        youtube_news = youtubelink(title=title, link=link)
        youtube_news.save()
        messages.success(request, 'News added!')
        return redirect('/admin_home/')


@login_required(login_url='/admin_login/')
def admin_add_youtube_view(request, dates, news_id):
    current_user = request.user

    youtubelink_query = youtubelink.objects.filter(date_uploaded=dates, id=news_id).first()
    context = {'youtubelink_query': youtubelink_query, 'current_user': current_user}
    return render(request, "admin_temp/add_youtube_link_view.html", context)


@login_required(login_url='/admin_login/')
def admin_add_youtube_edit(request, dates, news_id):
    current_user = request.user

    youtubelink_query = youtubelink.objects.filter(date_uploaded=dates, id=news_id).first()
    context = {'youtubelink_query': youtubelink_query, 'current_user': current_user}
    return render(request, "admin_temp/add_youtube_link_edit.html", context)


@login_required(login_url='/admin_login/')
def admin_add_breaking_news(request):
    current_user = request.user
    context = {'current_user': current_user}
    return render(request, "admin_temp/add_breaking_news.html", context)


@login_required(login_url='/admin_login/')
def admin_add_breaking_news_post(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        news_add = Breaking_news(title=title)
        news_add.save()
        messages.success(request, 'News added!')
        return redirect('/admin_home/')


@login_required(login_url='/admin_login/')
def admin_add_breaking_news_view(request, dates, news_id):
    current_user = request.user

    breaking_news_query = Breaking_news.objects.filter(date_uploaded=dates, id=news_id).first()
    context = {'breaking_news_query': breaking_news_query, 'current_user': current_user}
    return render(request, "admin_temp/add_breaking_news_view.html", context)


@login_required(login_url='/admin_login/')
def admin_add_breaking_news_edit(request, dates, news_id):
    current_user = request.user

    breaking_news_query = Breaking_news.objects.filter(date_uploaded=dates, id=news_id).first()
    context = {'breaking_news_query': breaking_news_query, 'current_user': current_user}
    return render(request, "admin_temp/add_breaking_news_edit.html", context)


@login_required(login_url='/admin_login/')
def admin_breaking_news_post(request, dates, news_id):
    if request.method == 'POST':
        title = request.POST.get("title")
        Breaking_news.objects.filter(date_uploaded=dates, id=news_id).update(title=title)
        return redirect('/admin_home/')


@login_required(login_url='/admin_login/')
def admin_smsPoll(request):
    current_user = request.user

    context = {'current_user': current_user}
    return render(request, "admin_temp/smsPoll.html", context)


@login_required(login_url='/admin_login/')
def admin_pollquestion(request):
    current_user = request.user

    context = {'current_user': current_user}
    return render(request, "admin_temp/pollquestion.html", context)


@login_required(login_url='/admin_login/')
def ads_page(request):

    current_user = request.user

    # 001
    ad_query_001 = ads_table.objects.filter(ads_num='001').last()

    # 002
    ad_query_002 = ads_table.objects.filter(ads_num='002').last()

    # 003
    ad_query_003 = ads_table.objects.filter(ads_num='003').last()

    # 004
    ad_query_004 = ads_table.objects.filter(ads_num='004').last()

    # 005
    ad_query_005 = ads_table.objects.filter(ads_num='005').last()

    # 006
    ad_query_006 = ads_table.objects.filter(ads_num='006').last()

    # 007
    ad_query_007 = ads_table.objects.filter(ads_num='007').last()

    # 008
    ad_query_008 = ads_table.objects.filter(ads_num='008').last()

    # 009
    ad_query_009 = ads_table.objects.filter(ads_num='009').last()

    # 010
    ad_query_010 = ads_table.objects.filter(ads_num='010').last()

    # 011
    ad_query_011 = ads_table.objects.filter(ads_num='011').last()

    # 012
    ad_query_012 = ads_table.objects.filter(ads_num='012').last()

    # 013
    ad_query_013 = ads_table.objects.filter(ads_num='013').last()

    # 014
    ad_query_014 = ads_table.objects.filter(ads_num='014').last()

    # 015
    ad_query_015 = ads_table.objects.filter(ads_num='015').last()

    # 016
    ad_query_016 = ads_table.objects.filter(ads_num='016').last()

    # 017
    ad_query_017 = ads_table.objects.filter(ads_num='017').last()

    # 018
    ad_query_018 = ads_table.objects.filter(ads_num='018').last()

    # 019
    ad_query_019 = ads_table.objects.filter(ads_num='019').last()

    # 020
    ad_query_020 = ads_table.objects.filter(ads_num='020').last()

    # 021
    ad_query_021 = ads_table.objects.filter(ads_num='021').last()

    # 022
    ad_query_022 = ads_table.objects.filter(ads_num='022').last()

    # 023
    ad_query_023 = ads_table.objects.filter(ads_num='023').last()

    # 024
    ad_query_024 = ads_table.objects.filter(ads_num='024').last()

    # 025
    ad_query_025 = ads_table.objects.filter(ads_num='025').last()

    # 026
    ad_query_026 = ads_table.objects.filter(ads_num='026').last()

    # 027
    ad_query_027 = ads_table.objects.filter(ads_num='027').last()

    # 028
    ad_query_028 = ads_table.objects.filter(ads_num='028').last()

    context = {'ad_query_001': ad_query_001, 'ad_query_002': ad_query_002, 'ad_query_003': ad_query_003,
               'ad_query_004': ad_query_004, 'ad_query_005': ad_query_005, 'ad_query_006': ad_query_006,
               'ad_query_007': ad_query_007, 'ad_query_008': ad_query_008, 'ad_query_009': ad_query_009,
               'ad_query_010': ad_query_010, 'ad_query_011': ad_query_011, 'ad_query_012': ad_query_012,
               'ad_query_013': ad_query_013, 'ad_query_014': ad_query_014, 'ad_query_015': ad_query_015,
               'ad_query_016': ad_query_016, 'ad_query_017': ad_query_017, 'ad_query_018': ad_query_018,
               'ad_query_019': ad_query_019, 'ad_query_020': ad_query_020, 'ad_query_021': ad_query_021,
               'ad_query_022': ad_query_022, 'ad_query_023': ad_query_023, 'ad_query_024': ad_query_024,
               'ad_query_025': ad_query_025, 'ad_query_026': ad_query_026, 'ad_query_027': ad_query_027,
               'ad_query_028': ad_query_028, 'current_user': current_user}
    return render(request, "admin_temp/ads_page.html", context)


@login_required(login_url='/admin_login/')
def add_ads_page(request, ads_id):
    current_user = request.user

    context = {'ads_id': ads_id, 'current_user': current_user}
    return render(request, "admin_temp/add_ads.html", context)


@login_required(login_url='/admin_login/')
def add_ads_page_post(request, ads_id):
    if request.method == 'POST':
        ad_title = request.POST.get('ad_title')
        img = request.FILES.get('img')

        ads_query = ads_table(title=ad_title, ads_num=ads_id, photo_img=img)
        ads_query.save()
        messages.success(request, 'Advertisement added!')
        return redirect('/ads_page/')


@login_required(login_url='/admin_login/')
def edit_ads_page(request, ads_id):

    current_user = request.user

    ads_query = ads_table.objects.filter(ads_num=ads_id).last()

    context = {'current_user': current_user, 'ads_query': ads_query}
    return render(request, "admin_temp/edit_ads.html", context)


@login_required(login_url='/admin_login/')
def del_ads(request, ads_id):
    del_query = ads_table.objects.get(ads_num=ads_id)

    del_image = del_query.photo_img
    del_image.delete()

    del_query.delete()

    messages.success(request, 'Ads Deleted')
    return redirect('/ads_page/')


@login_required(login_url='/admin_login/')
def admin_nationaNews(request):
    current_user = request.user

    sandhiya_news = sandhiya.objects.all().order_by('-id')
    paginator_sandhiya = Paginator(sandhiya_news, 10)
    page_number_sandhiya = request.GET.get('page1')
    try:
        page_obj_sandhiya_news = paginator_sandhiya.page(page_number_sandhiya)
    except PageNotAnInteger:
        page_obj_sandhiya_news = paginator_sandhiya.page(1)
    except EmptyPage:
        page_obj_sandhiya_news = paginator_sandhiya.page(paginator_sandhiya.num_pages)

    pradesh_news = pradesh.objects.all().order_by('-id')
    paginator_pradesh = Paginator(pradesh_news, 10)
    page_number_pradesh = request.GET.get('page2')
    try:
        page_obj_pradesh = paginator_pradesh.page(page_number_pradesh)
    except PageNotAnInteger:
        page_obj_pradesh = paginator_pradesh.page(1)
    except EmptyPage:
        page_obj_pradesh = paginator_pradesh.page(paginator_pradesh.num_pages)

    esthaniya_news = esthaniya.objects.all().order_by('-id')
    paginator_esthaniya = Paginator(esthaniya_news, 10)
    page_number_esthaniya = request.GET.get('page3')
    try:
        page_obj_esthaniya = paginator_esthaniya.page(page_number_esthaniya)
    except PageNotAnInteger:
        page_obj_esthaniya = paginator_esthaniya.page(1)
    except EmptyPage:
        page_obj_esthaniya = paginator_esthaniya.page(paginator_esthaniya.num_pages)

    manoranjan_news = manoranjan.objects.all().order_by('-id')
    paginator_manoranjan = Paginator(manoranjan_news, 10)
    page_number_manoranjan = request.GET.get('page4')
    try:
        page_obj_manoranjan = paginator_manoranjan.page(page_number_manoranjan)
    except PageNotAnInteger:
        page_obj_manoranjan = paginator_manoranjan.page(1)
    except EmptyPage:
        page_obj_manoranjan = paginator_manoranjan.page(paginator_manoranjan.num_pages)

    khelud_news = khelud.objects.all().order_by('-id')
    paginator_khelud = Paginator(khelud_news, 10)
    page_number_khelud = request.GET.get('page5')
    try:
        page_obj_khelud = paginator_khelud.page(page_number_khelud)
    except PageNotAnInteger:
        page_obj_khelud = paginator_khelud.page(1)
    except EmptyPage:
        page_obj_khelud = paginator_khelud.page(paginator_khelud.num_pages)

    context = {'sandhiya_news': page_obj_sandhiya_news, 'pradesh_news': page_obj_pradesh,
               'esthaniya_news': page_obj_esthaniya,'current_user': current_user,
               'manoranjan_news': page_obj_manoranjan, 'khelud_news': page_obj_khelud}
    return render(request, "admin_temp/nationaNews.html", context)


@login_required(login_url='/admin_login/')
def admin_add_national_news(request):

    current_user = request.user

    form = National_form()
    context = {'form': form, 'current_user': current_user}
    return render(request, "admin_temp/add_news.html", context)


@login_required(login_url='/admin_login/')
def admin_add_national_news_post(request):
    if request.method == 'POST':
        form = National_form(request.POST, request.FILES)

        if form.is_valid():
            title = form.cleaned_data.get("title")
            author = form.cleaned_data.get("author")
            location = form.cleaned_data.get("location")
            image = form.cleaned_data.get("img")
            news_summary = form.cleaned_data.get("news_summary")
            content = form.cleaned_data.get("content")
            scheduler = form.cleaned_data.get("scheduler")
            radio_button = form.cleaned_data.get("radio_button")

            if radio_button == 'सांघिय':
                news_add = sandhiya.objects.create(title=title, editor_name=author, photo_img=image, location=location,
                                                   description=content, news_summary=news_summary,
                                                   date_time_picker=scheduler)

                news_add.save()

                latest_add = Latest_news(title=title, editor_name=author, photo_img=image, location=location,
                                         description=content, news_summary=news_summary,
                                         date_time_picker=scheduler)
                latest_add.save()

                messages.success(request, 'news added!')
                return redirect('/admin_nationaNews/')

            if radio_button == 'पादेश':
                news_add = pradesh.objects.create(title=title, editor_name=author, photo_img=image, location=location,
                                                  description=content, news_summary=news_summary,
                                                  date_time_picker=scheduler)
                news_add.save()

                latest_add = Latest_news(title=title, editor_name=author, photo_img=image, location=location,
                                         description=content, news_summary=news_summary,
                                         date_time_picker=scheduler)
                latest_add.save()

                messages.success(request, 'news added!')
                return redirect('/admin_nationaNews/')

            if radio_button == 'स्थानिय':
                news_add = esthaniya.objects.create(title=title, editor_name=author, photo_img=image, location=location,
                                                    description=content, news_summary=news_summary,
                                                    date_time_picker=scheduler)
                news_add.save()

                latest_add = Latest_news(title=title, editor_name=author, photo_img=image, location=location,
                                         description=content, news_summary=news_summary,
                                         date_time_picker=scheduler)
                latest_add.save()

                messages.success(request, 'news added!')
                return redirect('/admin_nationaNews/')

            if radio_button == 'मनोरंजन':
                news_add = manoranjan.objects.create(title=title, editor_name=author, photo_img=image,
                                                     location=location,
                                                     description=content, news_summary=news_summary,
                                                     date_time_picker=scheduler)
                news_add.save()

                latest_add = Latest_news(title=title, editor_name=author, photo_img=image, location=location,
                                         description=content, news_summary=news_summary,
                                         date_time_picker=scheduler)
                latest_add.save()

                messages.success(request, 'news added!')
                return redirect('/admin_nationaNews/')

            if radio_button == 'खेलकुद':
                news_add = khelud.objects.create(title=title, editor_name=author, photo_img=image,
                                                 location=location,
                                                 description=content, news_summary=news_summary,
                                                 date_time_picker=scheduler)
                news_add.save()

                latest_add = Latest_news(title=title, editor_name=author, photo_img=image, location=location,
                                         description=content, news_summary=news_summary,
                                         date_time_picker=scheduler)
                latest_add.save()

                messages.success(request, 'news added!')
                return redirect('/admin_nationaNews/')


@login_required(login_url='/admin_login/')
def admin_national_news_view(request, news_types, dates, news_id):
    current_user = request.user

    if news_types == 'sandhiya':
        news_edit = sandhiya.objects.filter(id=news_id, date_uploaded=dates).last()
        context = {'news_edit': news_edit, 'current_user': current_user}
        return render(request, "admin_temp/view_news.html", context)

    if news_types == 'pradesh':
        news_edit = pradesh.objects.filter(id=news_id, date_uploaded=dates).last()
        context = {'news_edit': news_edit, 'current_user': current_user}
        return render(request, "admin_temp/view_news.html", context)

    if news_types == 'esthaniya':
        news_edit = esthaniya.objects.filter(id=news_id, date_uploaded=dates).last()
        context = {'news_edit': news_edit, 'current_user': current_user}
        return render(request, "admin_temp/view_news.html", context)

    if news_types == 'manoranjan':
        news_edit = manoranjan.objects.filter(id=news_id, date_uploaded=dates).last()
        context = {'news_edit': news_edit, 'current_user': current_user}
        return render(request, "admin_temp/view_news.html", context)

    if news_types == 'khelud':
        news_edit = khelud.objects.filter(id=news_id, date_uploaded=dates).last()
        context = {'news_edit': news_edit, 'current_user': current_user}
        return render(request, "admin_temp/view_news.html", context)


@login_required(login_url='/admin_login/')
def admin_national_news_edit(request, news_types, dates, news_id):

    current_user = request.user

    if news_types == 'sandhiya':
        news_edit = sandhiya.objects.get(id=news_id, date_uploaded=dates)

        form = National_edit_form(instance=news_edit)
        context = {'form': form, 'news_edit': news_edit, 'current_user': current_user}

        return render(request, "admin_temp/edit_news.html", context)

    if news_types == 'pradesh':
        news_edit = pradesh.objects.get(id=news_id, date_uploaded=dates)
        form = National_edit_form(instance=news_edit)
        context = {'form': form, 'news_edit': news_edit, 'current_user': current_user}
        return render(request, "admin_temp/edit_news.html", context)

    if news_types == 'esthaniya':
        news_edit = esthaniya.objects.get(id=news_id, date_uploaded=dates)
        form = National_edit_form(instance=news_edit)
        context = {'form': form, 'news_edit': news_edit, 'current_user': current_user}
        return render(request, "admin_temp/edit_news.html", context)

    if news_types == 'manoranjan':
        news_edit = manoranjan.objects.get(id=news_id, date_uploaded=dates)
        form = National_edit_form(instance=news_edit)
        context = {'form': form, 'news_edit': news_edit, 'current_user': current_user}
        return render(request, "admin_temp/edit_news.html", context)

    if news_types == 'khelud':
        news_edit = khelud.objects.get(id=news_id, date_uploaded=dates)
        form = National_edit_form(instance=news_edit)
        context = {'form': form, 'news_edit': news_edit, 'current_user': current_user}
        return render(request, "admin_temp/edit_news.html", context)


@login_required(login_url='/admin_login/')
def admin_national_news_post(request, news_types, dates, news_id):

    form = National_edit_form(request.POST, request.FILES)

    if form.is_valid():
        title = form.cleaned_data.get("title")
        author = form.cleaned_data.get("editor_name")
        location = form.cleaned_data.get("location")
        image = form.cleaned_data.get("photo_img")
        news_summary = form.cleaned_data.get("news_summary")
        content = form.cleaned_data.get("description")

        if news_types == 'sandhiya':
            sandhiya_news = sandhiya.objects.get(id=news_id)

            image_del = sandhiya_news.photo_img
            image_del.delete()

            sandhiya_news.title = title
            sandhiya_news.editor_name = author
            sandhiya_news.photo_img = image
            sandhiya_news.location = location
            sandhiya_news.news_summary = news_summary
            sandhiya_news.description = content
            sandhiya_news.save()

            messages.success(request, 'news updated!')
            return redirect('/admin_nationaNews/')

        if news_types == "pradesh":
            pradesh_news = pradesh.objects.get(id=news_id)

            image_del = pradesh_news.photo_img
            image_del.delete()

            pradesh_news.title = title
            pradesh_news.editor_name = author
            pradesh_news.photo_img = image
            pradesh_news.location = location
            pradesh_news.news_summary = news_summary
            pradesh_news.description = content
            pradesh_news.save()

            messages.success(request, 'news updated!')
            return redirect('/admin_nationaNews/')

        if news_types == "esthaniya":
            esthaniya_news = esthaniya.objects.get(id=news_id)

            image_del = esthaniya_news.photo_img
            image_del.delete()

            esthaniya_news.title = title
            esthaniya_news.editor_name = author
            esthaniya_news.photo_img = image
            esthaniya_news.location = location
            esthaniya_news.news_summary = news_summary
            esthaniya_news.description = content
            esthaniya_news.save()

            messages.success(request, 'news updated!')
            return redirect('/admin_nationaNews/')

        if news_types == "manoranjan":
            manoranjan_news = manoranjan.objects.get(id=news_id)

            image_del = manoranjan_news.photo_img
            image_del.delete()

            manoranjan_news.title = title
            manoranjan_news.editor_name = author
            manoranjan_news.photo_img = image
            manoranjan_news.location = location
            manoranjan_news.news_summary = news_summary
            manoranjan_news.description = content
            manoranjan_news.save()

            messages.success(request, 'news updated!')
            return redirect('/admin_nationaNews/')

        if news_types == "khelud":
            khelud_news = khelud.objects.get(id=news_id)

            image_del = khelud_news.photo_img
            image_del.delete()

            khelud_news.title = title
            khelud_news.editor_name = author
            khelud_news.photo_img = image
            khelud_news.location = location
            khelud_news.news_summary = news_summary
            khelud_news.description = content
            khelud_news.save()

            messages.success(request, 'news updated!')
            return redirect('/admin_nationaNews/')


@login_required(login_url='/admin_login/')
def admin_Interview(request):

    current_user = request.user

    antarbarta_news = antarbarta.objects.all().order_by('-id')
    paginator_antarbarta = Paginator(antarbarta_news, 10)
    page_number_antarbarta = request.GET.get('page')
    try:
        page_obj_antarbarta = paginator_antarbarta.page(page_number_antarbarta)
    except PageNotAnInteger:
        page_obj_antarbarta = paginator_antarbarta.page(1)
    except EmptyPage:
        page_obj_antarbarta = paginator_antarbarta.page(paginator_antarbarta.num_pages)
    context = {'antarbarta_news': page_obj_antarbarta, 'current_user': current_user}
    return render(request, "admin_temp/Interview.html", context)


@login_required(login_url='/admin_login/')
def admin_add_Interview(request, news_types):

    current_user = request.user

    form = add_news()
    context = {'news_types': news_types, 'form': form, 'current_user': current_user}
    return render(request, "admin_temp/add_news_other.html", context)


@login_required(login_url='/admin_login/')
def admin_add_Interview_post(request, news_types):
    form = add_news(request.POST, request.FILES)

    if form.is_valid():
        title = form.cleaned_data.get("title")
        author = form.cleaned_data.get("author")
        location = form.cleaned_data.get("location")
        image = form.cleaned_data.get("img")
        news_summary = form.cleaned_data.get("news_summary")
        content = form.cleaned_data.get("content")
        scheduler = form.cleaned_data.get("scheduler")

        if news_types == 'antarbarta':
            news_add = antarbarta(title=title, editor_name=author, photo_img=image, location=location,
                                  news_summary=news_summary, description=content,
                                  date_time_picker=scheduler)
            news_add.save()

            latest_add = Latest_news(title=title, editor_name=author, photo_img=image, location=location,
                                     description=content, news_summary=news_summary,
                                     date_time_picker=scheduler)
            latest_add.save()

            messages.success(request, 'News added!')
            return redirect('/admin_Interview/')

        if news_types == 'bichar_lekh':
            news_add = bichar_lekh(title=title, editor_name=author, photo_img=image, location=location,
                                   news_summary=news_summary, description=content, date_time_picker=scheduler)
            news_add.save()

            latest_add = Latest_news(title=title, editor_name=author, photo_img=image, location=location,
                                     description=content, news_summary=news_summary,
                                     date_time_picker=scheduler)
            latest_add.save()

            messages.success(request, 'News added!')
            return redirect('/admin_Thoughts/')

        if news_types == 'suchanapraviti':
            news_add = suchanapraviti(title=title, editor_name=author, photo_img=image, location=location,
                                      news_summary=news_summary, description=content,
                                      date_time_picker=scheduler)
            news_add.save()

            latest_add = Latest_news(title=title, editor_name=author, photo_img=image, location=location,
                                     description=content, news_summary=news_summary,
                                     date_time_picker=scheduler)
            latest_add.save()

            messages.success(request, 'News added!')
            return redirect('/admin_it_news/')

        if news_types == 'antarastriya':
            news_add = antarastriya(title=title, editor_name=author, photo_img=image, location=location,
                                    news_summary=news_summary, description=content,
                                    date_time_picker=scheduler)
            news_add.save()

            latest_add = Latest_news(title=title, editor_name=author, photo_img=image, location=location,
                                     description=content, news_summary=news_summary,
                                     date_time_picker=scheduler)
            latest_add.save()

            messages.success(request, 'News added!')
            return redirect('/admin_InternationalNews/')

        if news_types == 'sampadakiya':
            news_add = sampadakiya(title=title, editor_name=author, photo_img=image, location=location,
                                   news_summary=news_summary, description=content,
                                   date_time_picker=scheduler)
            news_add.save()

            latest_add = Latest_news(title=title, editor_name=author, photo_img=image, location=location,
                                     description=content, news_summary=news_summary,
                                     date_time_picker=scheduler)
            latest_add.save()

            messages.success(request, 'News added!')
            return redirect('/admin_Editorial/')


@login_required(login_url='/admin_login/')
def admin_Interview_view(request, news_types, dates, news_id):

    current_user = request.user

    if news_types == 'antarbarta':
        news_edit = antarbarta.objects.filter(id=news_id, date_uploaded=dates).last()
        context = {'news_edit': news_edit, 'current_user': current_user}
        return render(request, "admin_temp/view_news_other.html", context)

    if news_types == 'bichar_lekh':
        news_edit = bichar_lekh.objects.filter(id=news_id, date_uploaded=dates).last()
        context = {'news_edit': news_edit, 'current_user': current_user}
        return render(request, "admin_temp/view_news_other.html", context)

    if news_types == 'suchanapraviti':
        news_edit = suchanapraviti.objects.filter(id=news_id, date_uploaded=dates).last()
        context = {'news_edit': news_edit, 'current_user': current_user}
        return render(request, "admin_temp/view_news_other.html", context)

    if news_types == 'antarastriya':
        news_edit = antarastriya.objects.filter(id=news_id, date_uploaded=dates).last()
        context = {'news_edit': news_edit, 'current_user': current_user}
        return render(request, "admin_temp/view_news_other.html", context)

    if news_types == 'sampadakiya':
        news_edit = sampadakiya.objects.filter(id=news_id, date_uploaded=dates).last()
        context = {'news_edit': news_edit, 'current_user': current_user}
        return render(request, "admin_temp/view_news_other.html", context)


@login_required(login_url='/admin_login/')
def admin_Interview_edit(request, news_types, dates, news_id):

    current_user = request.user

    if news_types == 'antarbarta':
        news_edit = antarbarta.objects.get(id=news_id, date_uploaded=dates)
        form = add_news_edit(instance=news_edit)
        context = {'news_edit': news_edit, 'form': form, 'current_user': current_user}
        return render(request, "admin_temp/edit_news_other.html", context)

    if news_types == 'bichar_lekh':
        news_edit = bichar_lekh.objects.get(id=news_id, date_uploaded=dates)
        form = add_news_edit(instance=news_edit)
        context = {'news_edit': news_edit, 'form': form, 'current_user': current_user}
        return render(request, "admin_temp/edit_news_other.html", context)

    if news_types == 'suchanapraviti':
        news_edit = suchanapraviti.objects.get(id=news_id, date_uploaded=dates)
        form = add_news_edit(instance=news_edit)
        context = {'news_edit': news_edit, 'form': form, 'current_user': current_user}
        return render(request, "admin_temp/edit_news_other.html", context)

    if news_types == 'antarastriya':
        news_edit = antarastriya.objects.get(id=news_id, date_uploaded=dates)
        form = add_news_edit(instance=news_edit)
        context = {'news_edit': news_edit, 'form': form, 'current_user': current_user}
        return render(request, "admin_temp/edit_news_other.html", context)

    if news_types == 'sampadakiya':
        news_edit = sampadakiya.objects.get(id=news_id, date_uploaded=dates)
        form = add_news_edit(instance=news_edit)
        context = {'news_edit': news_edit, 'form': form, 'current_user': current_user}
        return render(request, "admin_temp/edit_news_other.html", context)


@login_required(login_url='/admin_login/')
def admin_Interview_post(request, news_types, dates, news_id):
    form = add_news(request.POST, request.FILES)

    if form.is_valid():
        title = form.cleaned_data.get("title")
        author = form.cleaned_data.get("editor_name")
        location = form.cleaned_data.get("location")
        image = form.cleaned_data.get("photo_img")
        news_summary = form.cleaned_data.get("news_summary")
        content = form.cleaned_data.get("description")

        if news_types == 'antarbarta':
            antarbarta_news = antarbarta.objects.get(id=news_id, date_uploaded=dates)

            image_del = antarbarta_news.photo_img
            image_del.delete()

            antarbarta_news.title = title
            antarbarta_news.editor_name = author
            antarbarta_news.photo_img = image
            antarbarta_news.location = location
            antarbarta_news.news_summary = news_summary
            antarbarta_news.description = content
            antarbarta_news.save()

            messages.success(request, 'news updated!')
            return redirect('/admin_Interview/')

        if news_types == 'bichar_lekh':
            bichar_lekh_news = bichar_lekh.objects.get(id=news_id, date_uploaded=dates)

            image_del = bichar_lekh_news.photo_img
            image_del.delete()

            bichar_lekh_news.title = title
            bichar_lekh_news.editor_name = author
            bichar_lekh_news.photo_img = image
            bichar_lekh_news.location = location
            bichar_lekh_news.news_summary = news_summary
            bichar_lekh_news.description = content
            bichar_lekh_news.save()

            messages.success(request, 'news updated!')
            return redirect('/admin_Thoughts/')

        if news_types == 'antarastriya':
            antarastriya_news = antarastriya.objects.get(id=news_id, date_uploaded=dates)

            image_del = antarastriya_news.photo_img
            image_del.delete()

            antarastriya_news.title = title
            antarastriya_news.editor_name = author
            antarastriya_news.photo_img = image
            antarastriya_news.location = location
            antarastriya_news.news_summary = news_summary
            antarastriya_news.save()

            messages.success(request, 'news updated!')
            return redirect('/admin_InternationalNews/')

        if news_types == 'sampadakiya':
            sampadakiya_news = sampadakiya.objects.get(id=news_id, date_uploaded=dates)

            image_del = sampadakiya_news.photo_img
            image_del.delete()

            sampadakiya_news.title = title
            sampadakiya_news.editor_name = author
            sampadakiya_news.photo_img = image
            sampadakiya_news.location = location
            sampadakiya_news.news_summary = news_summary
            sampadakiya_news.save()

            messages.success(request, 'news updated!')
            return redirect('/admin_Editorial/')

        if news_types == 'suchanapraviti':
            suchanapraviti_news = suchanapraviti.objects.get(id=news_id, date_uploaded=dates)

            image_del = suchanapraviti_news.photo_img
            image_del.delete()

            suchanapraviti_news.title = title
            suchanapraviti_news.editor_name = author
            suchanapraviti_news.photo_img = image
            suchanapraviti_news.location = location
            suchanapraviti_news.news_summary = news_summary
            suchanapraviti_news.save()

            messages.success(request, 'news updated!')
            return redirect('/admin_Editorial/')


@login_required(login_url='/admin_login/')
def admin_Thoughts(request):

    current_user = request.user

    bichar_lekh_news = bichar_lekh.objects.all().order_by('-id')
    paginator_bichar_lekh = Paginator(bichar_lekh_news, 10)
    page_number_bichar_lekh = request.GET.get('page')
    try:
        page_obj_bichar_lekh = paginator_bichar_lekh.page(page_number_bichar_lekh)
    except PageNotAnInteger:
        page_obj_bichar_lekh = paginator_bichar_lekh.page(1)
    except EmptyPage:
        page_obj_bichar_lekh = paginator_bichar_lekh.page(paginator_bichar_lekh.num_pages)
    context = {'bichar_lekh_news': page_obj_bichar_lekh, 'current_user': current_user}
    return render(request, "admin_temp/Thoughts.html", context)


@login_required(login_url='/admin_login/')
def admin_it_news(request):

    current_user = request.user

    suchanapraviti_news = suchanapraviti.objects.all().order_by('-id')
    paginator_suchanapraviti = Paginator(suchanapraviti_news, 10)
    page_number_suchanapraviti = request.GET.get('page')
    try:
        page_obj_suchanapraviti = paginator_suchanapraviti.page(page_number_suchanapraviti)
    except PageNotAnInteger:
        page_obj_suchanapraviti = paginator_suchanapraviti.page(1)
    except EmptyPage:
        page_obj_suchanapraviti = paginator_suchanapraviti.page(paginator_suchanapraviti.num_pages)

    context = {'suchanapraviti_news': page_obj_suchanapraviti, 'current_user': current_user}
    return render(request, "admin_temp/IT_news.html", context)


@login_required(login_url='/admin_login/')
def admin_InternationalNews(request):

    current_user = request.user

    antarastriya_news = antarastriya.objects.all().order_by('-id')
    paginator_antarastriya = Paginator(antarastriya_news, 10)
    page_number_antarastriya = request.GET.get('page')
    try:
        page_obj_antarastriya = paginator_antarastriya.page(page_number_antarastriya)
    except PageNotAnInteger:
        page_obj_antarastriya = paginator_antarastriya.page(1)
    except EmptyPage:
        page_obj_antarastriya = paginator_antarastriya.page(paginator_antarastriya.num_pages)

    context = {'antarastriya_news': page_obj_antarastriya, 'current_user': current_user}
    return render(request, "admin_temp/InternationalNews.html", context)


@login_required(login_url='/admin_login/')
def admin_Editorial(request):

    current_user = request.user

    sampadakiya_news = sampadakiya.objects.all().order_by('-id')
    paginator_sampadakiya = Paginator(sampadakiya_news, 10)
    page_number_sampadakiya = request.GET.get('page')
    try:
        page_obj_sampadakiya = paginator_sampadakiya.page(page_number_sampadakiya)
    except PageNotAnInteger:
        page_obj_sampadakiya = paginator_sampadakiya.page(1)
    except EmptyPage:
        page_obj_sampadakiya = paginator_sampadakiya.page(paginator_sampadakiya.num_pages)

    context = {'sampadakiya_news': page_obj_sampadakiya, 'current_user': current_user}
    return render(request, "admin_temp/Editorial.html", context)


@login_required(login_url='/admin_login/')
def admin_AboutUs(request):

    current_user = request.user

    about_us_1 = about_us.objects.all().first()
    context = {'about_us_1': about_us_1, 'current_user': current_user}
    return render(request, "admin_temp/AboutUs.html", context)


@login_required(login_url='/admin_login/')
def admin_AboutUs_edit(request):

    current_user = request.user

    form = about_us_post()
    context = {'form': form, 'current_user': current_user}
    return render(request, "admin_temp/aboutusedit.html", context)


@login_required(login_url='/admin_login/')
def admin_AboutUs_post(request):
    if request.method == 'POST':
        form = about_us_post(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/admin_home/')
    return render(request, "admin_temp/aboutusedit.html")


@login_required(login_url='/admin_login/')
def admin_setting(request):

    admin_all = request.user

    current_user = request.user

    context = {'admin_all': admin_all, 'current_user': current_user}
    return render(request, "admin_temp/setting.html", context)


@login_required(login_url='/admin_login/')
def admin_profile(request):

    current_user = request.user
    context = {'current_user': current_user}
    return render(request, "admin_temp/edit_profile.html", context)


@login_required(login_url='/admin_login/')
def admin_profile_post(request, authorization, admin_id):

    if request.method == "POST":
        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        contact = request.POST.get("contact")
        img = request.FILES.get("img")
        email_exists = False
        if request.user.id == admin_id:
            edit_admin = Profile.objects.get(user_id=admin_id, authorization=authorization)
            if edit_admin:
                if edit_admin.authorization == authorization:

                    admin_all = Profile.objects.all()
                    for items in admin_all:
                        if items.user.email == email:
                            email_exists = True
                            break

                    if email_exists:
                        messages.warning(request, 'Email already exists!')
                        return redirect('admin_profile')
                    else:
                        edit_admin.fullname = fullname
                        edit_admin.user.email = email
                        edit_admin.contact = contact
                        edit_admin.photo_img = img
                        edit_admin.save()

                        messages.success(request, 'Settings updated')
                        return redirect('/admin_setting/')


@login_required(login_url='/admin_login/')
def ns_setting_1(request):

    admin_all = request.user
    context = {'admin_all': admin_all}
    return render(request, "admin_temp/ns_setting_section/1.html", context)


@login_required(login_url='/admin_login/')
def admin_change_password_post(request, authorization, admin_id):

    current_pass = request.POST.get("password")
    new_pass_1 = request.POST.get("passOne")
    new_pass_2 = request.POST.get("passTwo")

    if request.user.id == admin_id:
        admin_user_news = Profile.objects.get(user_id=admin_id, authorization=authorization)

        if new_pass_1 == new_pass_2:

            if current_pass == admin_user_news.password:

                admin_user_news.user.password = new_pass_1
                admin_user_news.save()
                messages.success(request, 'Password changed')
                return redirect('/admin_setting/')

            elif current_pass != admin_user_news.password:
                messages.error(request, 'Current password does not match!')
                return redirect('/admin_setting/')

        else:
            messages.error(request, 'new password does not match!')
            return redirect('/admin_setting/')


@login_required(login_url='/admin_login/')
def ns_setting_2(request):
    current_user = request.user
    admin_users = Profile.objects.exclude(user_id=current_user.id).all()
    context = {'admin_users': admin_users}
    return render(request, "admin_temp/ns_setting_section/2.html", context)


@login_required(login_url='/admin_login/')
def ns_setting_3(request):

    admin_all = request.user

    context = {'admin_all': admin_all}
    return render(request, "admin_temp/ns_setting_section/3.html", context)


@login_required(login_url='/admin_login/')
def ns_setting_4(request):
    return render(request, "admin_temp/ns_setting_section/4.html")


@login_required(login_url='/admin_login/')
def admin_delete_news(request, news_types, dates, news_id):
    if news_types == "breaking_news":
        breaking_news_del = Breaking_news.objects.filter(date_uploaded=dates, id=news_id)
        breaking_news_del.delete()
        return redirect('/admin_home/')

    if news_types == "Latest_news":
        latest_news_del = Latest_news.objects.filter(date_uploaded=dates, id=news_id)
        latest_news_del.delete()
        return redirect('/admin_home/')

    if news_types == "sandhiya":
        sandhiya_news = sandhiya.objects.get(id=news_id, date_uploaded=dates)

        image_del = sandhiya_news.photo_img
        image_del.delete()

        sandhiya_news.delete()
        return redirect('/admin_nationaNews/')

    if news_types == "pradesh":
        pradesh_news = pradesh.objects.get(id=news_id, date_uploaded=dates)

        image_del = pradesh_news.photo_img
        image_del.delete()

        pradesh_news.delete()
        return redirect('/admin_nationaNews/')

    if news_types == "esthaniya":
        esthaniya_news = esthaniya.objects.get(id=news_id, date_uploaded=dates)

        image_del = esthaniya_news.photo_img
        image_del.delete()

        esthaniya_news.delete()
        return redirect('/admin_nationaNews/')

    if news_types == "manoranjan":
        manoranjan_news = manoranjan.objects.get(id=news_id, date_uploaded=dates)

        image_del = manoranjan_news.photo_img
        image_del.delete()

        manoranjan_news.delete()
        return redirect('/admin_nationaNews/')

    if news_types == "khelud":
        khelud_news = khelud.objects.get(id=news_id, date_uploaded=dates)

        image_del = khelud_news.photo_img
        image_del.delete()

        khelud_news.delete()
        return redirect('/admin_nationaNews/')

    if news_types == "antarbarta":
        antarbarta_news = antarbarta.objects.get(id=news_id, date_uploaded=dates)

        image_del = antarbarta_news.photo_img
        image_del.delete()

        antarbarta_news.delete()
        return redirect('/admin_Interview/')

    if news_types == "bichar_lekh":
        bichar_lekh_news = bichar_lekh.objects.get(id=news_id, date_uploaded=dates)

        image_del = bichar_lekh_news.photo_img
        image_del.delete()

        bichar_lekh_news.delete()
        return redirect('/admin_Thoughts/')

    if news_types == "suchanapraviti":
        suchanapraviti_news = suchanapraviti.objects.get(id=news_id, date_uploaded=dates)

        image_del = suchanapraviti_news.photo_img
        image_del.delete()

        suchanapraviti_news.delete()
        return redirect('/admin_it_news/')

    if news_types == "antarastriya":
        antarastriya_news = antarastriya.objects.get(id=news_id, date_uploaded=dates)

        image_del = antarastriya_news.photo_img
        image_del.delete()

        antarastriya_news.delete()
        return redirect('/admin_InternationalNews/')

    if news_types == "sampadakiya":
        sampadakiya_news = sampadakiya.objects.get(id=news_id, date_uploaded=dates)

        image_del = sampadakiya_news.photo_img
        image_del.delete()

        sampadakiya_news.delete()
        return redirect('/admin_Editorial/')

    if news_types == "grihaprista":
        grihaprista_news = grihaprista.objects.get(id=news_id, date_uploaded=dates)

        grihaprista_news.delete()
        return redirect('/admin_home/')

    if news_types == "youtube_link":
        youtubelink_news = youtubelink.objects.get(id=news_id, date_uploaded=dates)

        youtubelink_news.delete()
        return redirect('/ed')


def admin_login(request):
    if request.user.is_authenticated:
        return redirect('/admin_home/')
    else:
        form = login_form()
        context = {'form': form}
        return render(request, "admin_temp/login_page.html", context)


def admin_login_post(request):
    if request.method == 'POST':

        user_name = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=user_name, password=password)
        if user is not None:
            login(request, user)
            return redirect('/admin_home/')
        # A backend authenticated the credentials
        else:

            messages.warning(request, 'Wrong credentials!')
            return redirect('/admin_login/')
        # No backend authenticated the credentials



