from django.contrib import admin

from .models import Pages


class PagesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"page_link": ("title",)}
    list_display = ('id', 'title', 'position', 'page_link')
    list_display_links = ['title']
    list_editable = ['position', 'page_link']


admin.site.register(Pages, PagesAdmin)
