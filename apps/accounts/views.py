from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.utils.text import slugify
from django.views.generic import ListView

from .forms import ProductsForm, CustomUserCreationForm
from .models import UserAccount


class AccountUserLogoutView(LogoutView):
    template_name = 'accounts/logOut.html'


class AccountUserLoginView(LoginView):
    template_name = 'accounts/logIn.html'
    success_message = "Welcome back, you've successfully logged in"

    def authenticated(self):
        if self.is_authenticated:
            return "A user is already signed in."


def sign_up(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            user_account = UserAccount.objects.create(name=user.username, first_name=user.first_name,
                                                      last_name=user.last_name,
                                                      email=user.email, created_by=user)
            return redirect('homepage')

    else:
        form = CustomUserCreationForm()
        messages.warning(request, "Sign up failed, please try again")
    return render(request, 'accounts/signUp.html', {'form': form})


@login_required
def user_administration(request):
    AccountUser = request.user.AccountUser
    products = AccountUser.products.all()
    return render(request, 'accounts/userAdministration.html', {'UserAccount': AccountUser, 'products': products})


@login_required
def catalog_update(request):
    if request.method == 'POST':
        form = ProductsForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.UserAccount = request.user.AccountUser
            product.slug = slugify(product.title)
            product.save()
            return redirect('userAdministration')
    else:
        form = ProductsForm()
    return render(request, 'store/catalogUpdate.html', {'form': form})


class AccountUserListView(ListView):
    model = UserAccount
    paginate_by: 2
    context_object_name = 'accounts_list'
    template_name = 'accounts/list.html'
