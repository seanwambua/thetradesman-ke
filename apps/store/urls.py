from django.urls import path

from . import views

urlpatterns = [

    path('<slug:category_slug>/<int:pk>', views.ProductDetailView.as_view(), name='product'),
    path('<slug:category_slug>/<int:pk>', views.ServiceDetailView.as_view(), name='service'),



    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/', views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/', views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/', views.cart_detail, name='cart_detail'),
]
