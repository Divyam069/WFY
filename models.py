from django.db import models

# Create your models here.

class CategroyModel(models.Model):
    categoryName=models.CharField(max_length=100)
    categoryImage=models.ImageField(upload_to='category')
    def __str__(self) -> str:
        return self.categoryName
    
class ProductModel(models.Model):
    category=models.ForeignKey(CategroyModel,on_delete=models.CASCADE)
    productName=models.CharField(max_length=100)
    productPrice=models.PositiveBigIntegerField(max_length=5, default=0)
    productdescription=models.TextField(default=(""))
    productImage=models.ImageField(upload_to='Products')
    
    def __str__(self) -> str:
        return self.productName
    
class Register(models.Model):
    Name=models.CharField(max_length=10)
    Email=models.EmailField()
    Contact=models.PositiveBigIntegerField()
    password=models.CharField(max_length=10)
    def __str__(self) -> str:
        return self.Name
    
class Cartmodel(models.Model):
    orderId=models.CharField(max_length=100)
    userId=models.CharField(max_length=100)
    productId=models.CharField(max_length=100)
    quantity=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    totalprice=models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.orderId