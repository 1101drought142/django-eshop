from django.db import models
from utils.models import BaseSeo
#Custom classes
class Color(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название цвета')
    small_image = models.ImageField(upload_to='colors', verbose_name='Маленькое изображение')
    
    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'
        ordering = ['name']

class FlowerCountry(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название страны')
    small_image = models.ImageField(upload_to='flower_countries', verbose_name='Маленькое изображение')

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'
        ordering = ['name']

class FlowerType(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название типа')    

    class Meta:
        verbose_name = 'Тип цветка'
        verbose_name_plural = 'Типы цветков'
        ordering = ['name']

class Category(BaseSeo):
    name = models.CharField(max_length=255, verbose_name='Название категории')
    slug = models.SlugField(max_length=255, verbose_name='URL категории')
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', verbose_name='Родительская категория', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True, verbose_name='Активна')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

class Item(BaseSeo):
    name = models.CharField(max_length=255, verbose_name='Название товара')
    slug = models.SlugField(max_length=255, verbose_name='URL товара')
    category = models.ForeignKey(Category, verbose_name='Категория', blank=True, null=True, on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Описание товара')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена со скидкой', blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name='Активен')

    # put your custom fields here
    color = models.ForeignKey(Color, verbose_name='Цвет', blank=True, null=True, on_delete=models.SET_NULL)
    flowers_count = models.IntegerField(verbose_name='Количество цветов', blank=True, null=True)
    flower_type = models.ManyToManyField(FlowerType, verbose_name='Типы цветков')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['name']