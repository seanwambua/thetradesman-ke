from django.views.generic import DetailView, DeleteView

from .models import Services
from django.views.generic import DetailView, DeleteView

from .models import Services


class ServiceDetailView(DetailView):
    model = Services
    context_object_name = 'service'
    template_name = 'services/services.html'

class ServiceDeleteView(DeleteView):
    model = Services
    success_url ="AccountUser_admin"
   
    