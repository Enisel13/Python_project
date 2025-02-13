from django.contrib import admin
from .models import Category, Customer, Product, Order, Profile
from django.contrib.auth.models import User

admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Profile)


#Mix profile info and user info
class ProfileInline(admin.StackedInline):
    model = Profile

#Extend user model
class UserAdmin(admin.ModelAdmin):
    model = User
    field = ["username", "first_name", "last_name", "email"]
    inlines = [ProfileInline]

#Whenever we want to add these new things we first have to unregister the old way and then re-register the new way
#Unregister the old way
admin.site.unregister(User)

#Re-register the new way (Those re just Django things)
admin.site.register(User, UserAdmin)
