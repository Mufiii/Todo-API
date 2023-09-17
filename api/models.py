from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUsermanager(BaseUserManager):
    def create_user(self,email,username,password=None,**extra_fields):
        if not email :
          raise ValueError("user must hame email")
        
        user = self.model(
          email = self.normalize_email(email),
          username = username
        ) 
        user.set_password(password)
        user.save(using=self.db)
        return user
      
    def create_superuser(self,email,username,password=None):
      
        user = self.create_user(
           email,
           password = password,
           username = username  
        )
        user.is_admin = True
        user.save(using=self.db)
        return user




class User(AbstractBaseUser):
    email = models.EmailField(
      verbose_name="Email Address",
      max_length=100, 
      unique=True
    )
    username = models.CharField(max_length=100,unique=True)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    objects = MyUsermanager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
    