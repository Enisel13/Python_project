
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

    def add(self, product):
        product_id = str(product.id)

        #Logic
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price': str(product.price)}

        self.session.modified = True
        
    def __len__(self):
        return len(self.cart)#come through cart count up how many things are in it and then just return that
