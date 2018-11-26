from django.urls import path, re_path

from .views import Search, AboutSite, Contacts, SiteMap

urlpatterns = [
    path('search/', Search.as_view(), name='search'),
    re_path('search/?q=([A-Za-z0-9]+)&page=(\d+)/?$', Search.as_view()),
    path('aboutsite/', AboutSite.as_view(), name='aboutsite'),
    path('contacts/', Contacts.as_view(), name='contacts'),
    path('sitemap/', SiteMap.as_view(), name='sitemap'),
]
