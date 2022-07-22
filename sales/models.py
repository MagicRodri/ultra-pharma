
from django.db import models
from product.models import Product
from django.conf import settings
# Create your models here.

User = settings.AUTH_USER_MODEL

class Sale(models.Model):
    seller = models.ForeignKey(User,blank=True,null=True,on_delete=models.SET_NULL)
    product = models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    quantity = models.IntegerField()
    