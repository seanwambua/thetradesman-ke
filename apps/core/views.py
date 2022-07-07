from apps.products.models import Products
from django.shortcuts import render



def homepage(request):
    newest_products = Products.objects.all()
    return render(request, 'core/home.html', {'newest_products': newest_products})


def contact(request):
    return render(request, 'core/contact.html')
