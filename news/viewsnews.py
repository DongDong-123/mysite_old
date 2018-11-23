#!/usr/bin/python
from django.shortcuts import render
import time
from .models import News
# from django.http import HttpResponse
# import mod_pywebsocket
import math


def index(request):

    pages = request.GET.get('page')
    print('page', pages)
    if not pages:
        pages = 0
    begin = int(pages) * 20
    end = (int(pages) + 1) * 20
    # news = News.objects.all().order_by('-get_time', '-info_time')
    num = News.objects.count()
    news = News.objects.all().order_by('-get_time', '-info_time')[begin:end]
    begin = [2018, 11, 20]
    now = time.strftime("%Y-%m-%d-%H", time.localtime())
    now_list = now.split('-')
    page_num = math.ceil(num/20)
    print(page_num)
    current_page = int(pages)
    if current_page == 0:
        current_page = 1
    page_data = {'page_num': page_num, 'current_page': current_page}
    print(page_data)
    items = dict()
    items['year'] = int(now_list[0]) - begin[0]
    items['month'] = int(now_list[1]) - begin[1]
    items['day'] = int(now_list[2]) - begin[2]
    items['hour'] = int(now_list[3])
    assert isinstance(now, object)
    items['now'] = now

    content = {'content': news, 'nums': num, 'runtime': items, 'page_data': page_data}

    return render(request, 'news/index.html', content)


def lists(request, tid):
    commen = News.objects.filter(id=tid)

    content = {'commen': commen}
    return render(request, 'news/list.html', content)
