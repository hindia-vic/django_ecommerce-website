from ecommerce.models import Product
class Cart():
    def __init__(self,request):
        self.session=request.session
        #getting session key for already register user
        cart=self.session.get('session_key')
        #getting session key for new user
        if "session_key" not in request.session:
            cart=self.session['session_key']={}

        #ensuring cart keeps track of the user
        self.cart=cart

    def add(self,product,quantity):
        product_id=str(product.id)
        product_qty=str(quantity)

        if product_id in self.cart:
            pass
        else:
            self.cart[product_id]=int(product_qty)
        self.session.modified=True
    def __len__(self):
        return len(self.cart)
    def get_product(self):
        product_ids=self.cart.keys()
        products=Product.objects.filter(id__in=product_ids)
        return products
    def get_qty(self):
        quantities=self.cart
        return quantities
