from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect

from .models import *
from .forms import CommentForm
from pages.models import Pages


class Home(TemplateView):

    template_name = 'content/home.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        articles = Articles.objects.filter(article_publish=True)
        context['various'] = articles.order_by('?')[:5]
        context['recipes'] = articles.filter(
            recipe=True).order_by('-article_date')[:5]
        context['meta'] = Pages.objects.only(
            'title', 'metakey', 'metadesc').get(page_link='home')
        return context


class CatArticles(ListView):

    template_name = 'content/categories.html'

    model = Articles

    context_object_name = 'object_list'

    def get_context_data(self, **kwargs):
        context = super(CatArticles, self).get_context_data(**kwargs)
        cat = get_object_or_404(
                    Categories, category_link=self.kwargs['category_link'])

        p = self.object_list.filter(category_article_id=cat.id).order_by('id')
        paginator = Paginator(p, 6)

        cur_page = self.request.path_info[-1]

        if cur_page != '/':
            context['cur_page'] = ', страница %s' % cur_page

        try:
            arts = paginator.page(cur_page)
        except PageNotAnInteger:
            arts = paginator.page(1)
        except EmptyPage:
            arts = paginator.page(paginator.num_pages)

        context['articles'] = arts
        context['cat_krohi'] = cat
        return context


class ArticleDetail(DetailView):

    template_name = 'content/view_detailed.html'

    model = Articles

    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        context = super(ArticleDetail, self).get_context_data(**kwargs)
        context['get_comment'] = Comments.objects.filter(
            comments_article_id=self.object.id)
        context['form'] = CommentForm
        return context

    def post(self, request, **kwargs):
        if "but" not in request.POST:
            form = CommentForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.comments_article_id = kwargs['pk']
                post.save()
        else:
            request.session["e"] = True
            request.session.set_expiry(1)
        return HttpResponseRedirect(
            request.META.get('HTTP_REFERER') + '#comment')


class GetRecipes(ListView):

    template_name = 'content/recipes.html'

    context_object_name = 'object_list'

    def get_queryset(self):
        return Articles.objects.filter(
            recipe=True, article_publish=True).order_by('-article_date')

    def get_context_data(self, **kwargs):
        context = super(GetRecipes, self).get_context_data(**kwargs)
        paginator = Paginator(self.get_queryset(), 8)

        if self.kwargs:
            pg = self.kwargs['page_number']
        else:
            pg = self.request.path_info[-1]

        if pg != '/':
            context['cur_page'] = ', страница %s' % pg

        try:
            arts = paginator.page(pg)
        except PageNotAnInteger:
            arts = paginator.page(1)
        except EmptyPage:
            arts = paginator.page(paginator.num_pages)

        context['recipes'] = arts
        context['meta'] = Pages.objects.only(
            'title', 'metakey', 'metadesc').get(page_link='recipes')
        return context
