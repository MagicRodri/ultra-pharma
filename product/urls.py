from django.urls import path
from .views import (
    product_detail_view,
    product_search_view,
    product_create_view,
)

urlpatterns = [
    path('',product_search_view,name="product-search-view"),
    path('create/',product_create_view,name="product-create-view"),
    path('<slug:slug>/',product_detail_view,name="product-detail-view"),
]