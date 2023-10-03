from django.db import models

class BaseSeo(BaseSeo):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    keywords = models.TextField(verbose_name='Ключевые слова')
    class Meta:
        abstract = True

class NavBar(models.Model):
    pass