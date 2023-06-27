from django.contrib import admin
from .models import Product
# Register your models here.

class ProducAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}   # This will auto populate the slug field with the product name



admin.site.register(Product, ProducAdmin)