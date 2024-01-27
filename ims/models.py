from django.db import models
import qrcode
# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "catagories"

    def __str__(self):
        return self.name

class Product(models.Model):
    product_name = models.CharField(max_length=100, unique = True, verbose_name= "Product Name")
    quantity = models.PositiveIntegerField()
    product_category = models.ForeignKey(Category,  on_delete=models.CASCADE)
    purchased_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    seller = models.CharField(max_length=100)
    
    def __str__(self):
        return self.product_name
    
    @property
    def Tax(self):
        return (self.price * 15/100)
    
    @property
    def Total (self):
        return (self.price + self.Tax)
    

class Assign(models.Model):
      name = models.CharField(max_length = 200)
      department = models.ForeignKey(Department, on_delete = models.CASCADE)
      assigned_date = models.DateField(auto_now_add = True) 
      pro_id = models.PositiveIntegerField( unique = True, verbose_name = 'Product Id')
      category = models.ForeignKey(Category, on_delete = models.CASCADE)
      product = models.ForeignKey(Product, on_delete = models.DO_NOTHING)
      quantity = models.PositiveIntegerField()
      qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)

      def __str__(self):
        return self.name







