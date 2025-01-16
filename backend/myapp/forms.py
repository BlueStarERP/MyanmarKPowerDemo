from django import forms
from .models import *


class ULoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

class ItemsForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['item_name','category','price1','price2','price3','price4','package_unit','description','photo']
        widgets = {
            'item_name': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
            'category': forms.Select(attrs={'class': 'form-control col-md-6'}),
            'price1': forms.NumberInput(attrs={'class': 'form-control w-50'}),
            'price2': forms.NumberInput(attrs={'class': 'form-control w-50'}),
            'price3': forms.NumberInput(attrs={'class': 'form-control w-50'}),
            'price4': forms.NumberInput(attrs={'class': 'form-control w-50'}),
            'package_unit': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
            'description': forms.Textarea(attrs={'class': 'form-control col-md-6'}),
            'photo':forms.FileInput(attrs={'class':'form-control'}),
        }