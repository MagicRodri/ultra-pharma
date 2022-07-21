
from django.shortcuts import redirect, render
from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.db.models import Q
# Create your views here.

@login_required
def product_detail_view(request,slug=None):
    context={
        'obj':None
    }
    if slug is not None:
        try:
            product=Product.objects.get(slug=slug)
            context['obj']=product
        except Product.DoesNotExist:
            raise Http404
    return render(request,'products/detail.html',context=context)

@login_required
def product_search_view(request):
    context={}
    query=request.GET.get('q')
    if query is not None:
        lookups= Q(name__icontains=query) | Q(description__icontains=query)
        products=Product.objects.filter(lookups)
        context['products'] = products
        # print(query)
    else:
        context['search_err_msg']="No matching results for your research, please try again!"

    return render(request,'products/search.html',context=context)

@login_required
def product_create_view(request):
    form=ProductForm()
    context={
        'form':form
    }
    if request.method == 'POST':

        form=ProductForm(request.POST,request.FILES)

        if form.is_valid:
            product_obj=form.save()
            context['obj']=product_obj
            context['created']=True
            context['form']=ProductForm()
    return render(request,'products/create.html',context=context)