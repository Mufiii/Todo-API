from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(User)
class adminUser(admin.ModelAdmin):
  list_display = ('id','email','first_name','last_name','is_active')