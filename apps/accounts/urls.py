from django.urls import path

from .import views

urlpatterns = [

    # User Accounts    
    path('login', views.AccountUserLoginView.as_view(), name="login"),
    path('logout', views.AccountUserLogoutView.as_view(), name="logout"),
    path('stores', views.AccountUserListView.as_view(), name="stores"),
    path('signUp', views.sign_up, name="sign_up"),

    # Administration
    path('administration', views.AccountUser_admin, name="AccountUser_admin"),
    path('catalogUpdate', views.catalog_update, name="catalog_update"),
]
