
from django.shortcuts import redirect, render
from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def product_detail_view(request,id=None):
    context={
        'obj':None
    }
    if id is not None:
        try:
            product=Product.objects.get(id=id)
            context['obj']=product
        except:
            pass
    return render(request,'products/detail.html',context=context)

def product_search_view(request):
    context={}
    query_dict=request.GET
    # print(query_dict)
    obj=None
    try:
        query=int(query_dict.get('q'))
        obj=Product.objects.get(id=query)
        context['obj']=obj
        # print(query)
    except:
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