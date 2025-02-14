from django.db import models
from django.contrib.auth.models import User #We need to associate the shipping address with a particular user so we need our user model

#There we made a major change to our model we need to make a migration and push this into the database
class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255, null=True, blank=True)
    zipcode = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255)

    #Don`t pluralize address
    class Meta:
        verbose_name_plural = "Shipping address"

    def __str__(self):
        return f'Shipping address - {str(self.id)}'
