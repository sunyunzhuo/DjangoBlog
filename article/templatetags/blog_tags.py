# -*- coding: utf-8 -*-
from django import template
from django.db.models.aggregates import Count
from ..models import Article, Category, Tag
register = template.Library()


@register.simple_tag
def get_recent_posts(num=5):
    return Article.objects.all().order_by('-created_time')[:num]


@register.simple_tag
def archives():
    return Article.objects.dates('created_time', 'month', order='DESC')


@register.simple_tag
def get_categories():
    # 别忘了在顶部引入 Category 类
    return Category.objects.annotate(num_posts=Count('article')).filter(num_posts__gt=0)

@register.simple_tag
def get_tags():
    # 别忘了在顶部引入 Category 类
    return Tag.objects.annotate(num_posts=Count('article')).filter(num_posts__gt=0)