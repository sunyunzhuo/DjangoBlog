# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'article'  # 视图函数命名空间
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    # url(r'^index.html$', views.index, name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.ArticleDetailView.as_view(), name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchiveView.as_view(), name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
    url(r'^tag/(?P<pk>[0-9]+)/$', views.TagView.as_view(), name='tag'),
    url(r'^search/$', views.search, name='search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
