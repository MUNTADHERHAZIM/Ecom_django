from .cart import Cart

def cart(request):
    cart_instance = Cart(request)
    return {'Cart': cart_instance.cart}
