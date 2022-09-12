from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'products', views.ProductsView, 'products')
router.register(r'services', views.ServicesView, 'services')
router.register(r'policy', views.PolicyView, 'policy')


urlpatterns = [

    path('api/products/', views.getProducts, name='products'),
    path('api/products/<int:pk>', views.getProduct, name='product'),
    path('', include(router.urls)),
]
