from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm #we are saying "Take it from forms.py" and allow us to use it in our views.py"
from django import forms

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
            messages.success(request, ("You have registered successfully! Welcome!"))
            return redirect('home')
        
        else:
            messages.success(request, ("There was a problem registering, please try again!"))
            return redirect('register')

    else:
        return render(request, 'register.html', {'form':form}) #just show the page