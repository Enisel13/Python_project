from store.models import Product

class Cart():
    #request - anytime a user goes to the website he is making a request to view that website 
    def __init__(self, request):
        self.session = request.session

        #Get the current session key if it exist
        cart = self.session.get('session_key') #if the session key exist get it and ssign it to this cart variable

        #If the user is new, no session key, create one
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        #Make sure cart is available on all pages of site
        self.cart = cart

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)

        #Logic
        if product_id in self.cart:
            pass
        else:
            #self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)

        self.session.modified = True
        
    def __len__(self):
        return len(self.cart)#come through cart count up how many things are in it and then just return that

    #Allows us to see what is in the cart 
    def get_prods(self):
        #Whenever we add something to the cart it`s adding the ID of that product
        #So we can take that ID and use it to look up the product and see exactly what product is
        #Get ids from cart
        product_ids = self.cart.keys() #keys() because the product ID is pasted in a dictionary with the price (ID:price)

        #Use ids to lookup products in database model
        products = Product.objects.filter(id__in=product_ids) #всички id-та, които си намерил върни продуктите които отговарят

        #Return those looked up products
        return products
    
    def get_quants(self):
        quantities = self.cart
        return quantities
    
    def update(self, product, quantity):
        #This must be string and integer because our shopping cart is {'4':2}
        product_id = str(product)
        product_qty = int(quantity)
        #Get cart
        ourcart = self.cart
        #Update dictionary/cart
        ourcart[product_id] = product_qty

        self.session.modified = True
        thing = self.cart
        return thing

    def delete(self, product):
        product_id = str(product)
        #Delete from dictionary/cart
        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True

