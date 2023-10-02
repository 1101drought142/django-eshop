from cart.cart import Cart

def cart(request):
    return {'cart': Cart(request)}

def navbar_header():
    return None

def navbar_footer():
    return None

