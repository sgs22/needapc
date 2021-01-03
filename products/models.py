from django.db import models

"""
    Model for the products

    Saves all admin upload images to a 'product' media file and
    sorts them by date uploaded

"""
# class ProductDetail(models.Model):
#     name = models.CharField(max_length=120, blank=False) 
#     price = models.DecimalField(max_digits=6, decimal_places=2)
#     image = models.ImageField(upload_to='products/%Y/%m/%d/', max_length=255, null=True, blank=True)
#     brand = models.CharField(max_length=120, blank=True)
#     modelnumber = models.CharField(max_length=120, blank=True)
#     size = models.CharField(max_length=120, blank=True)
#     weight = models.CharField(max_length=120, blank=True)
#     # url = models.CharField(max_length=120, blank=True)
#     updated = models.DateTimeField(auto_now=True) # sets when saved
#     timestamp = models.DateTimeField(auto_now_add=True) # sets when added


class ProductDetail(models.Model):
    name = models.CharField(max_length=120, blank=False) 
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='products/%Y/%m/%d/', max_length=255, null=True, blank=True)
    url = models.CharField(max_length=120, blank=True)
    description_overview = models.CharField(max_length=120, blank=True)
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
    ram_size = models.CharField(max_length=120, blank=True)
    memory_type = models.CharField(max_length=120, blank=True)
    harddisk_type = models.CharField(max_length=120, blank=True)
    graphics_chipset_brand = models.CharField(max_length=120, blank=True)
    graphics_interface = models.CharField(max_length=120, blank=True)
    graphics_type = models.CharField(max_length=120, blank=True)
    operating_system = models.CharField(max_length=120, blank=True)
    battery_life = models.CharField(max_length=120, blank=True)
    weight = models.CharField(max_length=120, blank=True)
    featured = models.BooleanField(blank=True)
    updated = models.DateTimeField(auto_now=True) # sets when saved
    timestamp = models.DateTimeField(auto_now_add=True) # sets when added

    class Meta:
        ordering = ['name'] #LIFO ordering
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name

    