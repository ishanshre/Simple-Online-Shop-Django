from django.shortcuts import render, get_object_or_404
from .models import Product, Category
# Create your views here.

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(avaliable=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    context = {
        'category':category,
        'categories':categories,
        'products':products
    }
    return render(request, 'shop/index.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Prodcuct, id=id, slug=slug, avaliable=True)
    return render(request, 'shop/product_detail.html', {'product':product})

