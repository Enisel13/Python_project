from django.urls import path
# . означава, че се взима от текущата директория в случая текущата директория е store
from . import views

urlpatterns = [
    path('payment_success', views.payment_success, name='payment_success'),
    path('checkout', views.checkout, name='checkout'), 
    path('billing_info', views.billing_info, name='billing_info'), 
    

]
