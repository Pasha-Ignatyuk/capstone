from django.conf.urls import url
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
import os

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:product_id>', views.product, name='product'),
    path('laptops/', views.laptops, name='laptops'),
    path('phones/', views.phones, name='phones'),
   
]
