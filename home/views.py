from django.shortcuts import render
from products.models import Product, Category, Size


def index(request):
    """" A view to return the index page """

    return render(request, 'home/index.html')

def productIndex(request):


    context = {
        'products': products,
        'categories': categories
    }

    return render(request, 'home/index.html')
