from django.contrib.auth import views as auth_views
from django.urls import include, path
from . import views

urlpatterns = [
    path('become-vendor', views.SignUpView.as_view(), name="become_vendor"),
    path('vendor-admin', views.vendor_admin, name="vendor_admin"),
    path('logout', auth_views.LogoutView.as_view(), name="vendor_logout"),
    path('login', views.VendorLoginView.as_view(), name="vendor_login"),
]
