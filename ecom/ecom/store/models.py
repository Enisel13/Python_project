from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save

#Create customer profile
class Profile(models.Model):
    #We need to associste this new model with our Django authentication user model
    user = models.OneToOneField(User, on_delete=models.CASCADE) #we associste one profile with one user
    date_modified = models.DateTimeField(User, auto_now=True)
    phone =  models.CharField(max_length=20, blank=True)
    address1 = models.CharField(max_length=200, blank=True)
    address2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=20, blank=True)
    state = models.CharField(max_length=20, blank=True)
    zipcode = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=20, blank=True)
    old_cart = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.user.username

#Create a user profile by default when user signs up
def create_profile(sender, instance, created, **kwargs):
    if created: #We check if the user is newly created
        user_profile = Profile(user=instance) #createing a new user that information will becom this instance it will get passed into our profile
        user_profile.save()

#Automate the profile thing
#post_save - this will allow us to send a signal to our models to save something
#we call the function create_profile and the instance will be their current logged in instance
#and ceated will be what this post connect thing sends
post_save.connect(create_profile, sender=User)

#Categories of Products
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'categories'

#Costumers
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

#Products
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/products/')

    #Add Sale Stuff
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    
    def __str__(self):
        return self.name


#Customers orders
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, default='', blank=True)
    phone = models.CharField(max_length=20, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product