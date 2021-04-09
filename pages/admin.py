from django.contrib import admin

# Register your models here.
from .models import IndexPost

# class FeaturedAdmin(admin.Modeladmin):

admin.site.register(IndexPost)