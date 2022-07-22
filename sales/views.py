
from django.shortcuts import render
from .forms import SaleForm
# Create your views here.

def sale_view(request):
    form = SaleForm()
    context = {
        'form' : form,
    }
    if request.method == 'POST':
        form = SaleForm(request.POST)
        context['form'] = form # for gathering the uncleaned post data
        if form.is_valid():
            sale = form.save()
            sale_product = sale.product
            sale_product.quantity = sale_product.quantity - sale.quantity
            sale_product.save()
            context['success'] = True
    return render(request,'sales/sale.html',context=context)