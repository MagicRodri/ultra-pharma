from django.urls import reverse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
# Create your views here.

def login_view(request):
    if request.method=='POST':

        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect(reverse('home-view'))
    else:
        form=AuthenticationForm(request)

    context={
        'form':form
    }
    return render(request,'accounts/login.html',context=context)


def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect(reverse('login-view'))
    return render(request,'accounts/logout.html',context={})


def register_view(request):
    form=RegisterForm(request.POST or None)
    created = False
    if form.is_valid():
        form.save()
        created = True
        return redirect(reverse('home-view'))
    context={
        'form':form,
        'created': created
    }
    return render(request,'accounts/register.html',context=context)