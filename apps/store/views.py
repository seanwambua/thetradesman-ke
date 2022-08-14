from django.views.generic import DetailView, DeleteView

from .models import Products, Services


# --------------- PRODUCTS --------------------------------------------

class ProductDetailView(DetailView):
    model = Products
    context_object_name = 'product'
    template_name = 'store/parts/products/detail.html'


class ProductDeleteView(DeleteView):
    model = Products
    success_url = "userAdministration"


# --------------- SERVICES --------------------------------------------

class ServiceDetailView(DetailView):
    model = Services
    context_object_name = 'service'
    template_name = 'store/parts/services/detail.html'


class ServiceDeleteView(DeleteView):
    model = Services
    success_url = "userAdministration"
