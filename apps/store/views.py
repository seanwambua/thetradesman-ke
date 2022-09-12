from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from .models import Products,Services


# --------------- CART --------------------------------------------

def cart_add(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    service = Services.object.get(id=id)
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
