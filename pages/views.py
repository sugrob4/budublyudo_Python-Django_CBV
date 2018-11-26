import operator

from functools import reduce

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.contrib import messages
from django.db.models import Q
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

from content.models import Articles, Categories
from .models import Pages
from .forms import SendMail


class Search(ListView):

    model = Articles

    template_name = 'pages/search_results.html'

    context_object_name = 'object_list'

    paginate_by = 2

    def get_queryset(self):
        result = super(Search, self).get_queryset()
        query_list = self.request.GET.get('q').split()
        result = result.filter(
            reduce(operator.and_, (
                Q(article_title__icontains=q) for q in query_list)) |
            reduce(operator.and_, (
                Q(article_anons__icontains=q) for q in query_list)),
            article_publish=True).order_by('id')
        return result

    def dispatch(self, request, *args, **kwargs):
        query = request.GET.get('q')
        bad_search = request.META.get('HTTP_REFERER') or '/'
        pg = request.GET.get('page')
        if not query:
            if pg is not None:
                return render(request, self.template_name, {'page_obj': pg})
            else:
                messages.add_message(
                    request, messages.ERROR,
                    'Введите поисковый запрос.', extra_tags='search')
                return redirect(bad_search + "#ret")
        elif len(query) > 20:
            messages.add_message(
                request, messages.ERROR,
                'Введите не более 20 символов.', extra_tags='search')
            return redirect(bad_search + "#ret")
        elif len(query) < 3:
            messages.add_message(
                request, messages.ERROR,
                'Введите не менее 3-х символов', extra_tags='search')
            return redirect(bad_search + "#ret")
        else:
            self.get_queryset()
        return super(Search, self).dispatch(request, *args, **kwargs)


class AboutSite(TemplateView):
    template_name = 'pages/aboutsite.html'
    extra_context = {
        'about': get_object_or_404(Pages, page_link='aboutsite')}


class Contacts(FormView):
    template_name = 'pages/contacts.html'
    form_class = SendMail
    success_url = reverse_lazy('contacts')
    extra_context = {
        'meta': Pages.objects.only(
            'title', 'metakey', 'metadesc').get(page_link='contacts')}

    def form_valid(self, form):
        form.send_email()
        messages.add_message(
            self.request, messages.INFO,
            'Ваше письмо, отправленно успешно!', extra_tags='sendemail')
        return super().form_valid(form)


class SiteMap(TemplateView):
    template_name = 'pages/sitemap.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pages'] = Pages.objects.all()
        context['meta'] = context['pages'].only(
            'title', 'metakey', 'metadesc').get(page_link='sitemap')
        context['cat'] = Categories.objects.all()
        return context
