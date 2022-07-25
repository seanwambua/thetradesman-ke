from django.urls import path

from . import views

urlpatterns = [
    path('<slug:category_slug>/<int:pk>', views.ServiceDetailView.as_view(), name='service'),
]
