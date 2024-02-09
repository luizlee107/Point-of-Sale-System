from django.db import models

# Create your models here.
    
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    group = models.CharField(max_length=100)
    barcode = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
        
    
class Sale(models.Model):
    sale_code = models.CharField(max_length=100)
    product_list = models.CharField(max_length=1000)
    total_sale = models.DecimalField(max_digits=10, decimal_places=2)
    total_items = models.PositiveIntegerField()
    date = models.DateField(auto_now_add=True,null=True,blank=True) 
    
    def __str__(self):
        return self.sale_code
    
    
class Pos(models.Model):
    sale_code = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(null=True)   
    barcode = models.CharField(max_length=50,null=True,blank=True)
    price_unit= models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    date = models.DateField(auto_now_add=True,null=True,blank=True) 
    client_id = models.CharField(max_length=10,null=True,blank=True)
    total_items=models.PositiveIntegerField(null=True,blank=True)   
    tax=models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
  
    quantity = models.PositiveIntegerField(default=1)
    
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    group = models.CharField(max_length=100)
  
    def __str__(self):
        return f"{self.quantity} x {self.product.name} ({self.product.barcode})"
    
    
class Purchase(models.Model):
    purchase_code = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    price_buy = models.CharField(max_length=30)
    quantity = models.PositiveIntegerField()
    vendor=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name