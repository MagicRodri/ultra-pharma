from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','role','profile_photo']

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','role','profile_photo']