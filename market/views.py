from django.shortcuts import render
from .models import Product
# Create your views here.

def product_list(request):
    products = Product.objects.filter(active=True).order_by("-created_at")
    return render(request, "market/product_list.html", {"products": products})