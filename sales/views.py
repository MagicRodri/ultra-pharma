
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
        if form.is_valid:
            sale = form.save()
            context['success'] = True
    return render(request,'sales/sale.html',context=context)