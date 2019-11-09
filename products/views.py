from django.shortcuts import render, get_object_or_404
from products.models import Product

# Create your views here.
def index(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'products/index.html', {'product': product})
