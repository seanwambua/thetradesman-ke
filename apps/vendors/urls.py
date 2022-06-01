from django.urls import path

from .import views

urlpatterns = [

    # User Accounts    
    path('Login', views.VendorLoginView.as_view(), name="login"),
    path('Logout', views.VendorLogoutView.as_view(), name="logout"),
    path('Sign-Up', views.sign_up, name="sign_up"),

    # Administration
    path('vendor-admin', views.vendor_admin, name="vendor_admin"),
    path('add-product/', views.add_product, name="add_product"),
]
