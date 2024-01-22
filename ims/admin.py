from django.contrib import admin
from .models import Category, Department, Product
# Register your models here.
admin.site.register(Category)
admin.site.register(Department)
admin.site.register(Product)

# admin.site.register(Employee)