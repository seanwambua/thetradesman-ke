from django.urls import path

from . import views

urlpatterns = [
    path('', views.getRoutes, name='home'),
    path('api/products/', views.getProducts, name='products'),
    path('api/products/<int:pk>', views.getProduct, name='product'),
]
