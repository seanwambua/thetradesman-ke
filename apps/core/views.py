from django.shortcuts import render

from apps.store.models import Products, Services


def homepage(request):
    latest_services = Services.objects.filter(service_category=0)[0:6]
    newest_products = Products.objects.filter(product_category=0)[0:6]
    return render(request, 'core/home.html', {'newest_products': newest_products, 'latest_services': latest_services})


def contact(request):
    return render(request, 'core/contact.html')


def cart(request):
    return render(request, 'core/cart.html')
