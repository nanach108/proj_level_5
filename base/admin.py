from django.contrib import admin

# Register your models here.

from .models import Computers,Phones


admin.site.register(Computers)
admin.site.register(Phones)
# admin.site.register(User)