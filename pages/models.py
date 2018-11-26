from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Pages(models.Model):
    title = models.CharField(
        max_length=150, unique=True, blank=True, verbose_name='Страница')
    metakey = models.CharField(
        max_length=255, blank=True, verbose_name='Ключевые слова')
    metadesc = models.CharField(
        max_length=255, blank=True, verbose_name='Мета описание')
    page_link = models.SlugField(max_length=150, blank=True)
    page_text = RichTextUploadingField(
        blank=True, verbose_name='Текст страницы')
    position = models.SmallIntegerField(verbose_name='Позиция')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'pages'
        verbose_name = 'страница'
        verbose_name_plural = 'страницы'
        ordering = ['position']
