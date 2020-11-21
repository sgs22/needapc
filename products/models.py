from django.db import models

# Create your models here.
class ProductDetail(models.Model):
    name = models.CharField(max_length=120, blank=False) 
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='products/%Y/%m/%d/', max_length=255, null=True, blank=True)
    brand = models.CharField(max_length=120, blank=True)
    modelnumber = models.CharField(max_length=120, blank=True)
    size = models.CharField(max_length=120, blank=True)
    weight = models.CharField(max_length=120, blank=True)
    url = models.CharField(max_length=120, blank=True)
    updated = models.DateTimeField(auto_now=True) # sets when saved
    timestamp = models.DateTimeField(auto_now_add=True) # sets when added