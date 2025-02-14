from django.db import models
from django.contrib.auth.models import User #We need to associate the shipping address with a particular user so we need our user model
from store.models import Product

#There we made a major change to our model we need to make a migration and push this into the database
class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    shipping_full_name = models.CharField(max_length=255)
    shipping_email = models.CharField(max_length=255)
    shipping_address1 = models.CharField(max_length=255)
    shipping_address2 = models.CharField(max_length=255, null=True, blank=True)
    shipping_city = models.CharField(max_length=255)
    shipping_state = models.CharField(max_length=255, null=True, blank=True)
    shipping_zipcode = models.CharField(max_length=255, null=True, blank=True)
    shipping_country = models.CharField(max_length=255)

    #Don`t pluralize address
    class Meta:
        verbose_name_plural = "Shipping address"

    def __str__(self):
        return f'Shipping address - {str(self.id)}'
    
#Create order model
class Order(models.Model):
    #Foreign key
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    shipping_address = models.TextField(max_length=15000)#TextField is a box so we are goint 
                                                         #to take all of this stuff like
                                                         # (address1, address2, city...)
                                                         # and put them all in this one box like a 
                                                         #shipping label
    amount_paid = models.DecimalField(max_digits=30, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order - {str(self.id)}'

#Create order items model
class OrderItem(models.Model):
    #A bunch of Foreign keys
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    quantity = models.PositiveBigIntegerField(default=1)
    price = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return f'Order item - {str(self.id)}'
    