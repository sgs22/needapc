from django.db import models

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class IndexPost(models.Model):
    header = models.CharField(max_length=200, unique=True)
    subtitle = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='index/%Y/%m/%d/', max_length=255, null=True, blank=True)
    description = models.TextField(max_length=300, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.header