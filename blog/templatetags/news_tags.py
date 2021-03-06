from django import template

from ..models import Category

from django.db.models import Count, F


register = template.Library()


@register.simple_tag(name='get_list_categories')
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('blog/list_categories.html')
def show_categories():
    ctgrs = Category.objects.annotate(cnt=Count('news', filter=F('news__is_published'))).filter(cnt__gt=0)
    return {"ctgrs": ctgrs}


@register.inclusion_tag('blog/list_category_iss.html')
def show_category_iss():
    ctgrs = Category.objects.annotate(cnt=Count('newsiss')).filter(cnt__gt=0)
    return {"ctgrs": ctgrs}