from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from content.models import Articles, Categories
from pages.models import Pages


class ArticleSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Articles.objects.filter(article_publish=True).order_by('id')

    def lastmod(self, article):
        return article.article_date

    def location(self, article):
        return '/%s/%s-%s' % (
            article.category_article.category_link, article.id,
            article.article_link)


class CategorySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Categories.objects.all()

    def location(self, obj):
        return '/{}/'.format(obj.category_link)


class PagesSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Pages.objects.only('page_link')

    def location(self, obj):
        return reverse(obj.page_link)


sitemaps = {
    'articles': ArticleSitemap, 'pages': PagesSitemap,
    'categories': CategorySitemap}
