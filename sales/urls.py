from django.urls import path

from .views import (
    sale_view,
)

urlpatterns = [
    path('',sale_view,name='sale-view'),
]
