"""ultrapharma URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from .settings import DEBUG
from django.conf.urls.static import static

from .views import home_view
from product.views import (
    product_detail_view,
    product_search_view,
    product_create_view,
)

from accounts.views import(
    login_view,
    logout_view,
    register_view,
)

urlpatterns = [
    path('',home_view),
    path('products/',product_search_view),
    path('products/create/',product_create_view),
    path('products/<int:id>',product_detail_view),
    
    path('admin/', admin.site.urls),
    path('login/',login_view),
    path('logout/',logout_view),
    path('register/',register_view),
]  

if DEBUG :
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
