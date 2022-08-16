from django.urls import path

from . import views

urlpatterns = [
  #  path('<slug:category_slug>/<int:pk>', views.ProductDetailView.as_view(), name='product'),
    path('<slug:category_slug>/<int:pk>', views.ServiceDetailView.as_view(), name='service'),
    path('Delete', views.ProductDeleteView.as_view(), name='delete')
]
