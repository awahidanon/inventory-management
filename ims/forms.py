from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm

from .models import Assign, Product


class product_form(ModelForm):
   class Meta: 
        model = Product
        fields= ['product_name',  'quantity', 'product_category', 'purchased_date', 'price','seller']
        widgets = {
            'product_name': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'product_category': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'seller': forms.TextInput (attrs={'class': 'form-control'}),
            'purchased_date': forms.DateInput(format=('%Y-%m-%d'),  attrs={'class': 'form-control', 
               'placeholder': 'Select a date',
               'type': 'date'
              }),}
        


class Assign_form(ModelForm):
    class Meta:
        model = Assign

        fields = ['name', 'department', 'pro_id', 'product', 'quantity']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'pro_id': forms.TextInput(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control'}),
            
            }
        
    
class CustomUserLoginForm(AuthenticationForm):
   pass