from django.contrib import admin

# Register your models here.
from .models import ProductDetail, ProductImage, Review


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 5

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'timestamp')
    list_filter = ('timestamp',)
    search_fields = ['title', 'price']
    inlines = [ProductImageInline]

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'user','rating', 'body', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('user', 'email', 'body')
    actions = ['approve_reviews']

    def approve_reviews(self, request, queryset):
        queryset.update(approved=True) #approved TRUE on default for testing purposes

admin.site.register(ProductDetail, ProductAdmin)
admin.site.register(ProductImage)

