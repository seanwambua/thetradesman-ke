from django.urls import path

from .import views

urlpatterns = [
    # Authentication
    path('Sign-Up', views.become_vendor, name="become_vendor"),
    path('Login', views.VendorLoginView.as_view(), name="login"),
    path('Logout', views.VendorLogoutView.as_view(), name="logout"),

    # Administration
    path('vendor-admin', views.vendor_admin, name="vendor_admin"),
    path('add-product/', views.add_product, name="add_product"),
]
