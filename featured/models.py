from django.db import models

from products.models import ProductDetail

"""
    Initialises the status model for featured products
"""
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

"""
    Model for the featured products

    Saves all admin upload images to a featured media file and
    sorts them by date uploaded

    Featured posts ordered by newest first
"""
class FeaturedPost(models.Model):
    # product_id = models.ForeignKey(ProductDetail, on_delete=models.CASCADE) #get product ID from product model, TODO: FEATURED ID AND PRODUCT ID NEED TO BE THE SAME
    title = models.CharField(max_length=200, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='featured/%Y/%m/%d/', max_length=255, null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
