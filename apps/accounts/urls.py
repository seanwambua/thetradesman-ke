from django.urls import path

from .import views

urlpatterns = [

    # CustomUser Accounts
    path('login', views.CustomUserLoginView.as_view(), name="login"),
    path('logout', views.CustomUserLogoutView.as_view(), name="logout"),
    path('stores', views.CustomUserListView.as_view(), name="stores"),
    path('signUp', views.sign_up, name="sign_up"),

    # Administration
    path('administration', views.user_administration, name="AccountUser_admin"),
    path('catalogUpdate', views.catalog_update, name="catalog_update"),
]
