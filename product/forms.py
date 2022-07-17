
from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'

    
    # def clean(self):
    #     data=self.cleaned_data
    #     name=data.get('name')
    #     qs=Product.objects.filter(name__contains=name)
    #     if qs.exists():
    #         self.add_error('name',f"'{name}' is already in use ")
    #     return data