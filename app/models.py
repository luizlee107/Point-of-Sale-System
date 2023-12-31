from django.db import models

# Create your models here.
    
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    group = models.CharField(max_length=100)
    barcode = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
        
    
class Sale(models.Model):
    sale_code = models.CharField(max_length=100)
    product_list = models.CharField(max_length=1000)
    total_sale = models.DecimalField(max_digits=10, decimal_places=2)
    total_items = models.PositiveIntegerField()
    
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
    
    
class Purchase(models.Model):
    purchase_code = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    price_buy = models.CharField(max_length=30)
    quantity = models.PositiveIntegerField()
    vendor=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name