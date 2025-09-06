from django.contrib import admin
from django.urls import path, include
from market.views import product_list

urlpatterns = [
    path('', product_list, name="product_list"), # martet url
]