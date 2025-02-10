from .cart import Cart

#Create a context processor so our cart can work on all pages of the site
def cart(request):
    #Return the default data from out Cart
    return {'cart': Cart(request)}