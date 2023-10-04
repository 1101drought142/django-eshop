from django.db import models
from items.models import Item
from personalpage.models import CustomUser

class ModelCart(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name="Пользователь", on_delete=models.CASCADE)

    def save_to_db(self):
        pass
    pass

class ModalOrder(models.Model): 
    user = models.ForeignKey(CustomUser, verbose_name="Пользователь", on_delete=models.CASCADE)
    pass




class BaseItem(models.Model):
    item = models.ForeignKey(Item, verbose_name='Товар', on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name='Количество')

    class Meta:
        abstract = True 

class CartItem(BaseItem):
    cart = models.ForeignKey(ModelCart, verbose_name="Корзина", on_delete=models.CASCADE)
    pass

class OrderItem(BaseItem):
    order__save = models.ForeignKey(ModalOrder, verbose_name="Заказ", on_delete=models.CASCADE)
    pass