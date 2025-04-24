from django.contrib import admin
from .models import Category, Product

admin.site.register(Category)
# admin.site.register(Product)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'available')
    list_filter = ('available', 'category')
    search_fields = ('name',)

admin.site.register(Product, ProductAdmin)
