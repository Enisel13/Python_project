from django.shortcuts import render, redirect
from .models import Product, Category, Profile #from models.py Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, UpdateUserForm, ChangePasswordForm, UserInfoForm #we are saying "Take it from forms.py" and allow us to use it in our views.py"
from django import forms
from django.db.models import Q
import json #JavaScript object notation kind of like python dictionary
from cart.cart import Cart

def search(request):
    #Determine if they filled out the form
    if request.method == "POST":
        searched = request.POST['searched']
        #Query the products data base model
        #if we search table and Table icontains return the same result for both 
        searched = Product.objects.filter(Q(name__icontains=searched) | Q(description__icontains=searched) | Q(category__name__icontains=searched))
        
        #Test for null
        if not searched: 
            messages.success(request, "That product does not exist!")
            return render(request, "search.html", {'searched': None})
        else:
            return render(request, "search.html", {'searched':searched})
    else:
        return render(request, "search.html", {})

def update_info(request):
    if request.user.is_authenticated:
        #when a user is logged in we can find out what user that is by calling request.user.id
        current_user = Profile.objects.get(user__id=request.user.id) #find the user profile that has a user ID of.. (number)
        #instance=current_user - when someone goes to the web page  for the first time and click on the profile link to go to this page it will have his current information already in the form
        form = UserInfoForm(request.POST or None, instance=current_user)

        if form.is_valid():
            form.save() 
            messages.success(request, "Your info has been updated!")
            return redirect('home')
        else:
            return render(request, "update_info.html", {'form':form})
    #If they are not logged in
    else:
        messages.success(request, "You must be logged in!")
        return redirect('home')

def update_password(request):
    #Did they are logged in
    if request.user.is_authenticated:
        current_user = request.user
        #Did they fill out the form
        if request.method == 'POST':
            form = ChangePasswordForm(current_user, request.POST)
            #Is the form valid
            if form.is_valid():
                form.save()
                messages.success(request, "Your password has been updated")
                login(request, current_user)
                return redirect('update_user')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
                    return redirect('update_password')
             
                
        else:
            form = ChangePasswordForm(current_user)
            return render(request, "update_password.html", {'form':form})
    else:
        messages.success(request, "You must be logged in!")
        return redirect('home')


def update_user(request):
    if request.user.is_authenticated:
        #when a user is logged in we can find out what user that is by calling request.user.id
        current_user = User.objects.get(id=request.user.id) #getting the user from the model from the database
        #instance=current_user - when someone goes to the web page  for the first time and click on the profile link to go to this page it will have his current information already in the form
        user_form = UpdateUserForm(request.POST or None, instance=current_user)

        if user_form.is_valid():
            user_form.save() 

            login(request, current_user)
            messages.success(request, "User has been updated!")
            return redirect('home')
        else:
            return render(request, "update_user.html", {'user_form':user_form})
    #If they are not logged in
    else:
        messages.success(request, "You must be logged in!")
        return redirect('home')

def category_summary(request):
    #We need to grab all of our categories from our database model and then put them on the screen and turn them into URL
    categories = Category.objects.all() #this will grab everything from category model
    return render(request, 'category_summary.html', {"categories":categories})

def category(request, foo):
    #Replace Hyphens with Spaces
    foo = foo.replace('-', ' ')
    #Grab the category from the url
    #if the category do not exist we want to throw up an error
    try:
        #Look up the category
        category = Category.objects.get(name=foo)
        #Get all of the products in that cantegory
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'products':products, 'category':category})

    except:
        messages.success(request, ("That category does not exist!"))
        return redirect('home')

def product(request, pk):
    product = Product.objects.get(id=pk)#this will look up in product model and it will get the specific product number
    return render(request, 'product.html', {'product': product})


def home(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def about(request):
    return render(request, 'about.html', {})

def login_user(request):
    #this is saying "Did they fill out the form" 
    #so anytime somebody fills out that form and clicks the button they are posting to the page
    if request.method == "POST": #if they filled out the form do all this stuff here
        username = request.POST['username']
        password = request.POST['password']
        #now we need to authenticate
        user = authenticate(request, username=username, password=password)
        #now we need to check if the username and the password are correct
        if user is not None: #if the loggin is successful
            login(request, user) #this login function is this up here we imported

            #Do some shopping cart stuff
            current_user = Profile.objects.get(user__id=request.user.id)
            #Get their saved cart from database
            saved_cart = current_user.old_cart
            #Convert database string to python dictionary
            if saved_cart:
                #Convert in dictionary using JSON
                converted_cart = json.loads(saved_cart)
                #Add the loaded dictionary to our session
                #Get the cart
                cart = Cart(request)
                #Loop throught the cart and add the items from the database
                for key, value in converted_cart.items():
                    cart.db_add(product=key, quantity=value)


            messages.success(request, ("You have been logged in!"))
            return redirect('home')

        else:
            messages.success(request, ("There was an error, please try again"))
            return redirect('login')
    else: #if they didn`t filled out the form it means they just went to the web page
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out!"))
    return redirect('home') #we want to send user somewhere after he logged out

def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            #log in user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Username created, please fill out your user info below"))
            return redirect('update_info')
        
        else:
            messages.success(request, ("There was a problem registering, please try again!"))
            return redirect('register')

    else:
        return render(request, 'register.html', {'form':form}) #just show the page