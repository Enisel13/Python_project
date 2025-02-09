from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


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