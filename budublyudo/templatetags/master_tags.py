# -*- coding: utf-8 -*-
from django import template
from django.shortcuts import get_object_or_404

from content.models import Categories
from pages.models import Pages

register = template.Library()


@register.inclusion_tag('inc/header.html')
def header_obj():
    in_header = Categories.objects.exclude(
        in_header=0, class_in_header=False).order_by('in_header')
    pages = Pages.objects.only("title", "page_link")
    return {'in_header': in_header, 'pages': pages}


@register.inclusion_tag('inc/side_bar.html', takes_context=True)
def side_menu(context):
    return {'cat': Categories.objects.order_by('id'),
            'request': context['request'],
            'messages': context['messages']}


# @register.simple_tag(takes_context=True)
# def get_page(context):
#     request = context['request']
#     if request.path == '/':
#         page = get_object_or_404(Pages, slug='home')
#     else:
#         page = get_object_or_404(Pages, slug=request.path.strip("/"))
#     return page
