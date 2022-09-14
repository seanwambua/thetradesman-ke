import random

from django.shortcuts import render, get_object_or_404,  redirect
from django.views.generic import CreateView, TemplateView, DetailView, ListView, DeleteView
from django.contrib.auth.decorators import login_required
from cart.cart import Cart

from .models import Products, Services, Category

# --------------- PRODUCTS --------------------------------------------
class ProductListView(ListView):
    model = Products
    context_object_name = 'products_list'
    template_name = 'store/list.html'

class ProductDetailView(DetailView):
    model = Products
    context_object_name = 'product'
    template_name = 'store/parts/products/detail.html'

class ProductDeleteView(DeleteView):
    model = Products
    success_url ="accounts_admin"
   


# --------------- SERVICES --------------------------------------------
class ServiceListView(ListView):
    model = Services
    context_object_name = 'services_list'
    template_name = 'store/list.html'

class ServiceDetailView(DetailView):
    model = Services
    context_object_name = 'service'
    template_name = 'store/parts/services/detail.html'

class ServiceDeleteView(DeleteView):
    model = Services
    success_url ="vendor_admin"
   
    
# --------------- CART --------------------------------------------

def cart_add(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    service = Services.get(id=id)
    cart.add(product=product)
    return redirect("home")


def item_clear(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    service = Services.object.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


def item_increment(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    service = Services.object.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


def item_decrement(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    service = Services.object.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


def cart_detail(request):
    return render(request, 'cart/cart_detail.html')
