#!/usr/bin/python
from django.urls import path
from news import viewsnews

urlpatterns = [
    path('news/', viewsnews.index, name='newsindex'),
    path('news/list/(?P<tid>[0-9]+)', viewsnews.list, name='list'),

]
