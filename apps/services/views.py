import random

from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, TemplateView, DetailView, ListView, DeleteView

from .models import Services

class ServiceDetailView(DetailView):
    model = Services
    context_object_name = 'services'
    template_name = 'services/services.html'

class ServiceDeleteView(DeleteView):
    model = Services
    success_url ="vendor_admin"
   
    