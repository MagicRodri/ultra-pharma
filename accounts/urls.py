from unicodedata import name
from django.urls import path

from .views import(
    login_view,
    logout_view,
    register_view,
    profile_view,
    edit_profile_view
)

urlpatterns = [
    path('login/',login_view,name='login-view'),
    path('logout/',logout_view,name='logout-view'),
    path('profile/',profile_view,name='profile-view'),
    path('profile/edit',edit_profile_view,name='edit-profile-view'),
    path('register/',register_view,name='register-view'),
]
