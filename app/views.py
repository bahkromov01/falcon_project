from django.shortcuts import render
from app.models import Product
# Create your views here.


def index(requests):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(requests, 'app/index.html', context)
