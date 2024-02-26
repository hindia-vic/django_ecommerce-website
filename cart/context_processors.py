from .cart import Cart
#enable cart to work on all pages
def cart(request):
    return {'cart':Cart(request)}