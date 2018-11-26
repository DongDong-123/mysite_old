from blog import views
from django.urls import path


app_name = 'blog'
urlpatterns = [
    path(r'blog/index/', views.IndexView.as_view(), name='index'),
    path(r'blog/detail/<pk>/', views.PostDetialView.as_view(), name='detail'),
    # path(r'detail/<pk>/', views.detail, name='detail'),
    path(r'blog/archives/<year>/<month>/', views.ArchivesView.as_view(), name='archives'),
    path(r'blog/category/<pk>/', views.CategoryView.as_view(), name='category'),
    path(r'blog/tag/<pk>/', views.TagsView.as_view(), name='tag'),
    path(r'blog/contact/', views.contact, name='contact'),
    # path(r'blog/test3/', views.test3, name='test3'),
    # path(r'blog/about/', views.about, name='about'),
    path(r'blog/mail/', views.mail_me, name='mail_me'),
    path(r'blog/search/', views.search, name='search'),
]