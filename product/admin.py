
from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    
    list_display = ["name","slug"]
    search_fields = ["name","slug"]

admin.site.register(Product,ProductAdmin)