from django.contrib import admin
from .models import Product, Product_relations

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'price', 'created', 'slug']
    list_editable = ['price']
    prepopulated_fields = {'slug':('title',)}

@admin.register(Product_relations)
class Product_relationsAdmin(admin.ModelAdmin):
    list_display = ['product', 'images', 'size', 'color']