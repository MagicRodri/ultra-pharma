from django.shortcuts import render
from product.models import Product
from django.contrib.auth.decorators import login_required


@login_required
def home_view(request):
    fields_names=[f.name for f in Product._meta.get_fields()]
    product_qr=Product.objects.all()
    context={
        'objects':product_qr,
        'fields_names':fields_names
    }
    return render(request,'home.html',context=context)