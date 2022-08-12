from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from django.utils.text import slugify

from .forms import ProductsForm, CustomUserCreationForm
from .models import AccountUser
from django.core.paginator import Paginator
from django.contrib import messages



class AccountUserLogoutView(LogoutView):
    template_name = 'AccountUsers/logout.html'


class AccountUserLoginView(LoginView):
    template_name = 'AccountUsers/login.html'
    success_message = "Welcome back, you've succesfully logged in"

    def authenticated(self):
        if self.is_authenticated:
            return "A user is already signed in."


def sign_up(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            AccountUser = AccountUser.objects.create(name=user.username, first_name=user.first_name, last_name=user.last_name,
                                           email=user.email, created_by=user)
            return redirect('homepage')
            
    else:
        form = CustomUserCreationForm()
        messages.warning(request, "Sign up failed, please try again")
    return render(request, 'AccountUsers/signup.html', {'form': form})


@login_required
def user_administration(request):
    AccountUser = request.user.AccountUser
    products = AccountUser.products.all()
    return render(request, 'AccountUsers/useradministration.html', {'AccountUser': AccountUser, 'products': products})


@login_required
def catalog_update(request):
    if request.method == 'POST':
        form = ProductsForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.AccountUser = request.user.AccountUser
            product.slug = slugify(product.title)
            product.save()
            return redirect('AccountUser_admin')
    else:
        form = ProductsForm()
    return render(request, 'AccountUsers/catalogUpdate.html', {'form': form})

class AccountUserListView(ListView):
    model = AccountUser
    paginate_by: 2
    context_object_name = 'accounts_list'
    template_name = 'AccountUsers/list.html'

