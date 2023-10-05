from django.conf import settings
from cart.models import Cart, Order, CartItem, OrderItem
class Cart():
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                    'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def get_cartitem_list(self) -> list[CartItem]:
        cart_items = []
        for cart_item in self.cart:
            cart_item = CartItem(cart=self.cart, quantity=self.cart[cart_item]['quantity'])
            cart_items.append(cart_item)
        return cart_items
    


    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True