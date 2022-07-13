from django.urls import path

from .import views

urlpatterns = [

    # User Accounts    
    path('login', views.VendorLoginView.as_view(), name="login"),
    path('logout', views.VendorLogoutView.as_view(), name="logout"),
    path('stores', views.VendorListView.as_view(), name="stores"),
    path('signUp', views.sign_up, name="sign_up"),

    # Administration
    path('administration', views.vendor_admin, name="vendor_admin"),
    path('catalogUpdate', views.catalog_update, name="catalog_update"),
]
