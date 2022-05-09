from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from apps.products.models import Products




class ProductsForm(ModelForm):
    class Meta:
        model = Products
        fields = ['category', 'image', 'title', 'description', 'price']


class CustomUserCreationForm(forms.Form):
    username = forms.CharField(label='Enter Username', min_length=4, max_length=150)
    first_name = forms.CharField(label='Enter First name:')
    last_name = forms.CharField(label='Enter Last name:')
    email = forms.EmailField(label='Enter Email')
    introduction = forms.CharField(label='Please introduce yourself: (This intro will be seen by your clients)')
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        requested_name = User.objects.filter(username=username)
        if requested_name.count():
            raise ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")

        return password2

    def save(self):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.first_name,
            self.last_name,
            self.cleaned_data['email'],
            self.cleaned_data['password1'],
            self.introduction,
        )
        return user
