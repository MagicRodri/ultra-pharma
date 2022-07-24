from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class User(AbstractUser):
    DIRECTOR = "DIRECTOR"
    MANAGER = "MANAGER"
    EMPLOYEE = "EMPLOYEE"
    CUSTOMER = "CUSTOMER"
    DEFAULT = "DEFAULT"

    ROLES_CHOICES = (
        (DIRECTOR,'Director'),
        (MANAGER,'Manager'),
        (EMPLOYEE,'Employee'),
        (CUSTOMER,'Customer'),
        (DEFAULT,'Default')
    )
    profile_photo = models.ImageField(upload_to ='users',blank = True)
    role = models.CharField(max_length=25 , choices=ROLES_CHOICES, default= DEFAULT)

    def create(self,user = None):
        created = True
        if user is not None :
            if self.role != user.role :
                if self.role == self.DIRECTOR:
                    user.save()
                elif self.role == self.MANAGER and user.role != self.DIRECTOR:
                    user.save()
                elif self.role == self.EMPLOYEE and user.role not in (self.DIRECTOR,self.MANAGER):
                    user.save()
                else:
                    created = False
            else :
                created =False
        else :
            created = False
                