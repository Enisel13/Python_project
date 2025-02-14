from django.db import models
from django.contrib.auth.models import User #We need to associate the shipping address with a particular user so we need our user model

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
