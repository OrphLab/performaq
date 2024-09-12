from django.db import models
from django.contrib.auth.models import User 

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name
    

class Product(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_prodcuts")
    name = models.CharField(max_length=15, default="aToolkit")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    buyers = models.ManyToManyField(User, related_name='bought_products', blank=True)
    tags = models.ManyToManyField(Tag, related_name='products', blank=True)
    
    def __str__(self):
        return self.name

class ProductFile(models.Model):
    name=models.CharField(max_length=25)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='product_files/')
    description = models.CharField(max_length=255, blank = True)
    
    def __str__(self):
        return self.file.name


