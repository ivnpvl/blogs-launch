from django.shortcuts import get_object_or_404, render

from .models import Group, Post

AMOUNT_DISPLAYED_POSTS: int = 10


def index(request):
    posts = Post.objects.all()[:AMOUNT_DISPLAYED_POSTS]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:AMOUNT_DISPLAYED_POSTS]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
