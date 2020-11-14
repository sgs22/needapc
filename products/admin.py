from django.contrib import admin

# Register your models here.
from .models import ProductDetail

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'timestamp')
    list_filter = ('timestamp',)
    search_fields = ['title', 'price']

admin.site.register(ProductDetail, ProductAdmin)
