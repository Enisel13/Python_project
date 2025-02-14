from django.urls import path
# . означава, че се взима от текущата директория в случая текущата директория е store
from . import views

urlpatterns = [
    path('payment_success', views.payment_success, name='payment_success'), 
    

]
