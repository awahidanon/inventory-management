from django.contrib import admin
from .models import Category, Department, Product, Assign
from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.register(Category)
admin.site.register(Department)
admin.site.register(Product)
admin.site.register(Assign)


# admin.site.register(Employee)