
from django.urls import reverse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, EditProfileForm
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
    online_user = request.user
    form=RegisterForm(request.POST or None)
    created = False
    if form.is_valid():
        new_user = form.save(commit=False)
        created = online_user.create(new_user)
        # return redirect(reverse('home-view'))
    context={
        'form':form,
        'created': created
    }
    return render(request,'accounts/register.html',context=context)

@login_required
def profile_view(request):
    user = request.user
    return render(request,'accounts/profile.html',context={'user':user})


@login_required
def edit_profile_view(request):
    current_user = request.user
    form = EditProfileForm(instance = current_user)
    if request.method == 'POST':
        form = EditProfileForm(request.POST,request.FILES,instance = current_user)
        if form.is_valid():
            updated_user = form.save()
            return redirect(reverse('profile-view'))
    context = {'form' : form}
    return render(request,'accounts/edit_profile.html',context=context)