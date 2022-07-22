
from django.db import models
from django.db.models.signals import pre_save,post_save
from .utils import slugify_instance_name
from django.db.models import Q
# Create your models here.

class ProductManager(models.Manager):
    
    def search(self,query=None):
        if query is None or query == "":
            return self.get_queryset().none() # []
        else:
            lookups = Q(name__icontains=query) | Q(description__icontains=query)
            return self.get_queryset().filter(lookups)

class Product(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(unique=True,max_length=64,null=True,blank=True)
    description = models.TextField(blank=True)
    img = models.ImageField(upload_to='product',blank=True,default=None)
    quantity = models.IntegerField(default=0)
    price = models.FloatField()

    objects = ProductManager()

    # def set_quantity(self,quantity):
    #     if quantity >= 0:
    #         self.quantity = quantity
    #     self.save()

    def save(self,*args,**kargs):

        # if self.slug is None :
        #     self.slug = slugify(self.name)
        super().save(*args,**kargs)

    def __str__(self) -> str:
        return self.name

def product_pre_save(sender,instance,*args,**kargs):
    # This is run before the save method
    # print("pre_save")
    if instance.slug is None :
        slugify_instance_name(instance,save=False)

pre_save.connect(product_pre_save,sender=Product)

def product_post_save(sender,instance,created,*args,**kargs):
    # This is run after the save method
    # print('post_save')
    if created :
        slugify_instance_name(instance, save=True)

post_save.connect(product_post_save,sender=Product)