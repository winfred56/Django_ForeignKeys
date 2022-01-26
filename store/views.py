from django.shortcuts import render
from django.template import context
from .models import Product, Product_relations

def all_products(request):
    products=Product.objects.all()
    context = {
        'products':products
    }
    return render(request, 'store/index.html', context)

def detail(request, slug):
    product = Product.objects.get(slug=slug)
    context = {'product':product}
    return render(request,'store/detail.html',context)

