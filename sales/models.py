
from itertools import product
from django.db import models
from product.models import Product
from django.conf import settings

from django.db.models.signals import post_save
# Create your models here.

User = settings.AUTH_USER_MODEL

class Sale(models.Model):
    PENDING = "PENDING"
    SOLD = "SOLD"

    STATUS_CHOICES = (
        (PENDING,'Pending'),
        (SOLD,'Sold')
    )
    seller = models.ForeignKey(User,blank=True,null=True,on_delete=models.SET_NULL)
    # product = models.ManyToManyField(Product)
    product = models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, choices = STATUS_CHOICES,default = PENDING)

# def sale_post_save(instance,sender,created,*args,**kargs):
#     if created:
#         product = instance.product
#         product.set_quantity(product.quantity - instance.quantity)

# post_save.connect(sale_post_save,sender=Sale)