from django.db import models
from django.contrib.auth.models import User

"""
    Model for the products
"""
class ProductDetail(models.Model):
    name = models.CharField(max_length=120, blank=False) 
    price = models.DecimalField(max_digits=6, decimal_places=2)
    #image = models.ImageField(upload_to='products/%Y/%m/%d/', max_length=255, null=True, blank=True) #this might change to img urls...
    url = models.CharField(max_length=120, blank=True)
    description = models.TextField(max_length=300, blank=True)
    brand = models.CharField(max_length=120, blank=True)
    dimensions = models.CharField(max_length=120, blank=True)
    model_number = models.CharField(max_length=120, blank=True)
    manufacturer = models.CharField(max_length=120, blank=True)
    colour = models.CharField(max_length=120, blank=True)
    formfactor = models.CharField(max_length=120, blank=True)
    screen_size = models.CharField(max_length=120, blank=True)
    resolution = models.CharField(max_length=120, blank=True)
    processor_brand = models.CharField(max_length=120, blank=True)
    processor_type = models.CharField(max_length=120, blank=True)
    processor_speed = models.CharField(max_length=120, blank=True)
    processor_corecount = models.CharField(max_length=120, blank=True)
    ram_size = models.CharField(max_length=120, blank=True)
    memory_type = models.CharField(max_length=120, blank=True)
    harddisk_type = models.CharField(max_length=120, blank=True)
    graphics_chipset_brand = models.CharField(max_length=120, blank=True)
    graphics_interface = models.CharField(max_length=120, blank=True)
    graphics_type = models.CharField(max_length=120, blank=True)
    operating_system = models.CharField(max_length=120, blank=True)
    battery_life = models.CharField(max_length=120, blank=True)
    weight = models.CharField(max_length=120, blank=True)
    featured = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True) # sets when saved
    timestamp = models.DateTimeField(auto_now_add=True) # sets when added

    class Meta:
        ordering = ['name'] #LIFO ordering
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    name = models.CharField(max_length=255)
    product = models.ForeignKey(ProductDetail, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='productImages/%Y/%m/%d/', max_length=255, null=True, blank=True)
    default = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Product Image"
        verbose_name_plural = "Product Images"

    def __str__(self):
        return self.name

    def default(self):
        return self.images.filter(default=True).first() #default image shows as main image on product


SCORE = (
    (1,"Very Poor"),
    (2,"Poor"),
    (3,"Okay"),
    (4,"Good"),
    (5,"Excellent")
)

class Review(models.Model):
    product = models.ForeignKey(ProductDetail, on_delete=models.CASCADE,related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=SCORE, default=3)
    title = models.CharField(max_length=200, unique=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True) #default true for testing

    class Meta:
        ordering = ['created_on'] 

    def __str__(self):
        return 'Review {} by {}'.format(self.title, self.user)