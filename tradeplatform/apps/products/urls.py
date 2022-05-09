from django.urls import path

from . import views

urlpatterns = [
    path('<slug:category_slug>/<slug:product_slug>', views.ProductDetailView.as_view(), name='product')
]
