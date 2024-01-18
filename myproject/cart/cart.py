from myapp.models import Product

class Cart:
    def __init__(self, request):
        self.session = request.session

        # Get the current session key if it exists
        cart = self.session.get('session_key')

        # If the user is new, no session key! Create one!
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        # Make sure cart is available on all pages of the site
        self.cart = cart

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = int(quantity)  # Ensure quantity is an integer
        # Logic
        if product_id  in self.cart:
            pass
        else:
            self.cart[product_id] = int(product_qty)

        self.session.modified = True

    def __len__(self):
        return len(self.cart)
    
    def get_prods(self):
        # Get ids of products in cart
        product_ids = self.cart.keys()
        
        # Get the product objects and return them   
        products = Product.objects.filter(id__in=product_ids)
        return products 

def cart_delete(self, product):
        # Implement logic for deleting a product from the cart
    pass

def cart_update(self, product, quantity):
        # Implement logic for updating the quantity of a product in the cart
    pass
