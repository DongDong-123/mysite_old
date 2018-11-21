#!/usr/bin/python
from django.shortcuts import render
import time
from .models import News


def index(request):
    news = News.objects.all().order_by('-get_time', '-info_time')
    num = News.objects.count()
    begin = [2018, 11, 20]
    now = time.strftime("%Y-%m-%d-%H", time.localtime())
    now_list = now.split('-')

    items = dict()
    items['year'] = int(now_list[0]) - begin[0]
    items['month'] = int(now_list[1]) - begin[1]
    items['day'] = int(now_list[2]) - begin[2]
    items['hour'] = int(now_list[3])
    items['now'] = now

    # print(now)
    content = {'content': news, 'nums': num, 'runtime': items}

    return render(request, 'news/index.html', content)


def list(request, tid):
    commen = News.objects.filter(id=tid)
    content = {'commen': commen}
    return render(request, 'news/list.html', content)
