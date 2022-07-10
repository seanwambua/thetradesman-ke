from django.urls import path

from .import views

urlpatterns = [

    # User Accounts    
    path('Login', views.VendorLoginView.as_view(), name="login"),
    path('Logout', views.VendorLogoutView.as_view(), name="logout"),
    path('Stores', views.VendorListView.as_view(), name="stores"),
    path('Sign Up', views.sign_up, name="sign_up"),

    # Administration
    path('User Administration', views.vendor_admin, name="vendor_admin"),
    path('Update Catalog', views.add_to_catalog, name="add_to_catalog"),
]
