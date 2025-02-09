from django.urls import path
# . означава, че се взима от текущата директория в случая текущата директория е store
from . import views

urlpatterns = [
    path('', views.home, name='home'), #homepage
    path('about/', views.about, name='about'),
    path('login/', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.register_user, name='register'),
]
