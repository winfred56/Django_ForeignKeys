from django.shortcuts import render
from .models import Product, Product_relations

def all_products(request):
    product=Product.objects.all()
    context = {
        'product':product
    }
    return render(request, 'store/index.html', context)


