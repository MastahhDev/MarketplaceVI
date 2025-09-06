from django.contrib import admin
from .models import Product
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'seller', 'price', 'active', 'created_at')
    search_fields = ('title', 'description', 'seller__username')
    list_filter = ('active', 'created_at', 'seller')