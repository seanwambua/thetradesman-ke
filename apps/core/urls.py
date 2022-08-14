from django.urls import path

from . import views

urlpatterns = [
    path('', views.latest_additions, name='homepage'),
    path('contact', views.contact, name='contact'),
    path('cart', views.cart, name='cart'),
]
