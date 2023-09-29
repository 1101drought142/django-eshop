from django.db import models
from items.models import Item


class Cart(models.Model):
    pass

class BaseItem(models.Model):
    item = models.ForeignKey(Item, verbose_name='Товар', on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name='Количество')

    class Meta:
        abstract = True 


class CartItem(BaseItem):
    pass