from django.contrib import admin

# Register your models here.
from .models import ProductDetail, Review

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'timestamp')
    list_filter = ('timestamp',)
    search_fields = ['title', 'price']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'user','rating', 'body', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('user', 'email', 'body')
    actions = ['approve_reviews']

    def approve_reviews(self, request, queryset):
        queryset.update(approved=True)

admin.site.register(ProductDetail, ProductAdmin)

