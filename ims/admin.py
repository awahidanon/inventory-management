from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Assign, Category, Department, Product

# Register your models here.
admin.site.register(Category)
admin.site.register(Department)
admin.site.register(Product)
admin.site.register(Assign)


# admin.site.register(Employee)