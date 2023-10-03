from django.db import models

# Create your models here.
class TextPage(models.Model):
    name = models.CharField(max_length=200, verbose_name="Имя")
    content = models.TextField(verbose_name="Содержание")
    photo = models.FieldFile(upload_to='photos', blank=True, verbose_name="Фото")