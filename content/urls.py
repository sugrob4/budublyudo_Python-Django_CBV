from django.urls import path, re_path

from .views import Home, CatArticles, ArticleDetail, GetRecipes

urlpatterns = [
    path('recipes/', GetRecipes.as_view(), name='recipes'),
    re_path('^recipes/page=(?P<page_number>\d+)/?$', GetRecipes.as_view()),

    path('', Home.as_view(), name='home'),
    path('<slug:category_link>/', CatArticles.as_view(), name='cat'),
    re_path('^(?P<category_link>[a-z-]+)/page=(\d+)/?$',
            CatArticles.as_view()),
    path('<slug:category_link>/<int:pk>-<slug:article_link>/',
         ArticleDetail.as_view(), name='detail'),
    path('add_comment/<int:pk>', ArticleDetail.as_view(), name='add_comment'),
]
