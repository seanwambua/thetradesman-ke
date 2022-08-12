from apps.store.models import Products, Services
from django.shortcuts import render




def homepage(request):
    latest_services = Products.objects.filter(category=1)[0:6]
    newest_products = Products.objects.filter(category=2)[0:6]
    latest_ventures = Products.objects.filter(category=3)[0:6]
    return render(request, 'core/home.html', {'newest_products': newest_products, 'latest_services': latest_services, 'latest_ventures': latest_ventures})


def contact(request):
    return render(request, 'core/contact.html')

def cart(request):
    return render(request, 'core/cart.html')
