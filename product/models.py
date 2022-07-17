
from email.policy import default
from django.db import models

# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField(blank=True)
    img=models.ImageField(upload_to='product',blank=True,default=None)
    quantity=models.IntegerField(default=1)
    price=models.FloatField()