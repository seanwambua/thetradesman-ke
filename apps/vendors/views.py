from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from django.utils.text import slugify

from .forms import ProductsForm, CustomUserCreationForm
from .models import Vendor
from django.core.paginator import Paginator
from django.contrib import messages

class SuccessMessageMixin:
    success_message = ''

class VendorLogoutView(LogoutView):
    template_name = 'vendors/vendor_logout.html'


class VendorLoginView(LoginView):
    template_name = 'vendors/vendor_login.html'
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
            Vendor.objects.create(name=user.username, first_name=user.first_name, last_name=user.last_name,
                                           email=user.email, created_by=user)
            return redirect('homepage')
            
    else:
        form = CustomUserCreationForm()
        messages.warning(request, "Sign up failed, please try again")
    return render(request, 'vendors/vendor_signup.html', {'form': form})


@login_required
def vendor_admin(request):
    vendor = request.user.vendor
    products = vendor.products.all()
    return render(request, 'vendors/vendor_admin.html', {'vendor': vendor, 'products': products})


@login_required
def catalog_update(request):
    if request.method == 'POST':
        form = ProductsForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.vendor = request.user.vendor
            product.slug = slugify(product.title)
            product.save()
            return redirect('vendor_admin')
    else:
        form = ProductsForm()
    return render(request, 'vendors/catalogUpdate.html', {'form': form})

class VendorListView(ListView):
    model = Vendor
    paginate_by: 2
    context_object_name = 'vendors'
    template_name = 'vendors/vendors_list.html'

