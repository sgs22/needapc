from django.views import generic
from .models import Post
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

"""
    Filter the posts to only display those that are published
    and order them by newest first in queryset
"""
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/blog.html'

"""
    View for seeing the blog post on a single page
"""
class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

"""
    Get the blog post details else 404

    Show form for user so they can comment on post when blog
    is in detailed view

    Render field order requires for form
"""
def post_detail(request, slug):
    template_name = 'blog/post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})