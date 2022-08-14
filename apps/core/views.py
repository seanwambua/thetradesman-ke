from django.shortcuts import render

from apps.store.models import Products, Services


def latest_additions(request):
    latest_services = Services.objects.all()[0:6]
    latest_products = Products.objects.all()[0:6]
    return render(request, 'core/home.html', {'latest_products': latest_products, 'latest_services': latest_services})


def contact(request):
    return render(request, 'core/contact.html')


def cart(request):
    return render(request, 'core/cart.html')
