from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import BlogPost
from .forms import BlogPostForm

#def index(request):
#    """The home page for our Blog"""
#    return render(request, 'blogs/index.html')

def index(request):
    """Show all of the blogposts."""
    blogposts = BlogPost.objects.order_by('-date_added')
    context = {'blogposts': blogposts}
    return render(request, 'blogs/index.html', context)

def new_post(request):
    """Add a new post."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = BlogPostForm()
    else:
        # POST data submitted; process data.
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:index'))

    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)

def edit_post(request, post_id):
    """Edit an existing post."""
    post = BlogPost.objects.get(id=post_id)

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = BlogPostForm(instance=post)
    else:
        # POST data submitted; process data.
        form = BlogPostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:index'), args=[post.id])
    
    context = {'form': form}
    return render(request, 'blogs/edit_post.html', context)