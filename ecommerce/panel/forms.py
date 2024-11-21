from django import forms 
from main.models import *

class CategoryForm(forms.ModelForm):
  name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

  class Meta:
    model = Category
    fields = '__all__'

class ProductForm(forms.ModelForm):
  name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  category = forms.ModelChoiceField(queryset=Category.objects.all(),  widget=forms.Select(attrs={'class':'form-control'}))
  price = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'form-control'}))
  discount = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
  desc = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
  weight = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'form-control'}))

  class Meta:
    model = Product
    fields = '__all__'
