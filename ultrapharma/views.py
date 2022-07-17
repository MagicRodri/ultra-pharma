from django.shortcuts import render
from product.models import Product
from product.forms import ProductForm
from django.forms.models import model_to_dict

def home_view(request):
    fields_names=[f.name for f in Product._meta.get_fields()]
    product_qr=Product.objects.all()
    context={
        'objects':product_qr,
        'fields_names':fields_names
    }
    return render(request,'home.html',context=context)