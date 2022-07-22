from itertools import product
from pyexpat import model
from django import forms
from .models import Sale


class SaleForm(forms.ModelForm):
    
    class Meta:
        model = Sale
        fields = '__all__'

    def clean(self):
        cleaned_data = self.cleaned_data # a dict
        product = cleaned_data.get('product')
        print(product)
        quantity = cleaned_data.get('quantity')
        if quantity > product.quantity:
            raise forms.ValidationError("You can't sell more than available in stock")
        return cleaned_data