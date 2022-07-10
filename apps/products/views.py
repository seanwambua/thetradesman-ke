import random

from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, TemplateView, DetailView, ListView, DeleteView

from .models import Products, Category

class ProductDetailView(DetailView):
    model = Products
    context_object_name = 'product'
    template_name = 'products/product.html'

class ProductDeleteView(DeleteView):
    # specify the model you want to use
    model = Products
     
    # can specify success url
    # url to redirect after successfully
    # deleting object
    success_url ="vendor_admin"
   
    