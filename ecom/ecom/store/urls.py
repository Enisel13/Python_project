from django.urls import path
# . означава, че се взима от текущата директория в случая текущата директория е store
from . import views

urlpatterns = [
    path('', views.home, name='home'), #homepage
]
