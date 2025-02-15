from django.shortcuts import render, redirect
from cart.cart import Cart

from payment.forms import ShippingForm, PaymentForm
from payment.models import ShippingAddress
from django.contrib import messages

def billing_info(request):
    if request.POST:#If they come from the previous page, if they filled out the 
                    #form for the shipping info, click the billing button and they have moved forward
        #Get the cart
        cart = Cart(request)
        cart_products = cart.get_prods
        quantities = cart.get_quants
        totals = cart.cart_total()
        #Check to see if user is logged in
        if request.user.is_authenticated:
            #Get the billing form
            billing_form = PaymentForm()
            #We can grab that form (in checkout page) that they filled out on the previous screen with a request.POST
            #but we can assign that to a shipping form variable and use it on the page 
            return render(request, "payment/billing_info.html", {"cart_products":cart_products, "quantities":quantities, "totals":totals, "shipping_info":request.POST, "billing_form":billing_form })
        else:
            #Not logged in
            #Get the billing form
            billing_form = PaymentForm()
            return render(request, "payment/billing_info.html", {"cart_products":cart_products, "quantities":quantities, "totals":totals, "shipping_info":request.POST, "billing_form":billing_form })

        shipping_form = request.POST
        return render(request, "payment/billing_info.html", {"cart_products":cart_products, "quantities":quantities, "totals":totals, "shipping_form":shipping_form})
    else:
        messages.success(request, "Access Denied")
        return redirect('home')

def checkout(request):
#Get the cart
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    totals = cart.cart_total()

    if request.user.is_authenticated:
        #Check out as logged in user
        #Shipping user 
        shipping_user = ShippingAddress.objects.get(user__id=request.user.id)
        #Shipping from
        shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
        return render(request, "payment/checkout.html", {"cart_products":cart_products, "quantities":quantities, "totals":totals, "shipping_form":shipping_form})
    else:
        #Check out as guest
        shipping_form = ShippingForm(request.POST or None) #I removed nstance=shipping_user because the guests don`t have aved information
        return render(request, "payment/checkout.html", {"cart_products":cart_products, "quantities":quantities, "totals":totals, "shipping_form":shipping_form})



def payment_success(request):
    return render (request, "payment/payment_success.html", {})

