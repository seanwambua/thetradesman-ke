from django.views.generic import DetailView, DeleteView

from .models import Products
from django.views.generic import DetailView, DeleteView

from .models import Products, Services


# --------------- PRODUCTS --------------------------------------------

class ProductDetailView(DetailView):
    model = Products
    context_object_name = 'product'
    template_name = 'products/product.html'


class ProductDeleteView(DeleteView):
    model = Products
    success_url = "AccountUser_admin"


# --------------- SERVICES --------------------------------------------

class ServiceDetailView(DetailView):
    model = Services
    context_object_name = 'service'
    template_name = 'services/services.html'


class ServiceDeleteView(DeleteView):
    model = Services
    success_url = "vendor_admin"
