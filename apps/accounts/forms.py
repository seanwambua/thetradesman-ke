from email import message
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from apps.store.models import Products, Service
from django.contrib import messages

class ProductsForm(ModelForm):
    class Meta:
        model = Products
        fields = [
            'category',
            'image',
            'title',
            'description',
            'price'
        ]

class CustomUserCreationForm(forms.Form):
#    profile_photo = forms.ImageField(label='Please upload a photo for your profile')
    first_name = forms.CharField(label='Please enter your first name:',min_length=2, max_length=150)
    last_name = forms.CharField(label='Please enter your last name:',min_length=2, max_length=150)
    email = forms.EmailField(label='Please enter your official email')
    username = forms.CharField(label='Please enter your Business Name', min_length=4, max_length=150)
    new_password = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    confirmation_password = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        requested_name = User.objects.filter(username=username)
        if requested_name.exists():
            raise ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        email_user = User.objects.filter(email=email)
        if email_user.count():
            messages.error(self,"Invalid Email")
            raise ValidationError("This email address is already linked to another account. Please try a different email.")
            
        return email

    def clean_password2(self):
        new_password = self.cleaned_data.get('new_password')
        confirmation_password = self.cleaned_data.get('confirmation_password')

        if new_password and confirmation_password and new_password != confirmation_password:
            raise ValidationError("Passwords don't match. Please try again.")

        return confirmation_password

    def save(self):
        user = User.objects.create_user(
            self.cleaned_data['username'],
          #  profile_photo = self.cleaned_data['profile_photo'],
            first_name = self.cleaned_data['first_name'],
            last_name = self.cleaned_data['last_name'],
            email = self.cleaned_data['email'],
            password = self.cleaned_data['new_password'],
        )
        return user
