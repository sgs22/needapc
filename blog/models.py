from django.db import models
from django.contrib.auth.models import User

"""
    Initialises the status model for blog posts
"""
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

"""
    Model for the blog posts

    Displays the blog posts newest first - LIFO Ordering
"""
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField(max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on'] #LIFO ordering
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"

    def __str__(self):
        return self.title

"""
    Model for the comments on blogs

    Displays the comments from oldest to newest - FIFO ordering
"""
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on'] #FIFO ordering

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)