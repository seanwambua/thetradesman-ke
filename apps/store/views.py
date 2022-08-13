from django.views.generic import DetailView, DeleteView

from .models import Products
from django.views.generic import DetailView, DeleteView

from .models import Products, Services


# --------------- PRODUCTS --------------------------------------------

class ProductDetailView(DetailView):
    model = Products
    context = 'product'
    template_name = 'store/parts/products/detail.html'


class ProductDeleteView(DeleteView):
    model = Products
    success_url = "userAdministration"


# --------------- SERVICES --------------------------------------------

class ServiceDetailView(DetailView):
    model = Services
    context = 'service'
    template_name = 'store/parts/products/detail'


class ServiceDeleteView(DeleteView):
    model = Services
    success_url = "userAdministration"
