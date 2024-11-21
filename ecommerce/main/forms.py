from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from main.models import *

class RegistrationFrom(UserCreationForm):
  username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
  password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class LoginForm(AuthenticationForm):
  username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class OrderForm(forms.ModelForm):
  payment_type = forms.CharField(widget=forms.RadioSelect(choices=Order.PAYMEENT_TYPES))
  desc = forms.CharField(widget=forms.Textarea(attrs={'rows':'3'}))

  class Meta:
    model = Order
    exclude = ['cart', 'order_status']


class ProductImageForm(forms.ModelForm):
  
  class Meta:
    models = ProductImage
    fields = ['image']