from django.contrib import admin
from .models import Post, Comment

"""
    Checks if current logged in user is an admin/staff
    then will display the current comments on each blog post that are awaiting
    to be approved.

    ModelAdmin is to register the model in the admin panel and the
    above fields are used to structure the admin panels
"""
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

"""
    Display the queryset of all blog posts and registers if they need
    to be updated on whether they are published or draft.

    ModelAdmin is to register the model in the admin panel and the
    above fields are used to structure the admin panels.
"""
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    actions = ['publish', 'draft']

    def publish(self, request, queryset):
        queryset.update(status=1)
    def draft(self, request, queryset):
        queryset.update(status=0)
  
admin.site.register(Post, PostAdmin)