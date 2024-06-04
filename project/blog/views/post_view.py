from django.shortcuts import render
from blog.models import Post

def post(request, slug):
    post = Post.objects.get(slug=slug,)


    context = {
        'post': post,
    }

    return render(request, 'blog/pages/post.html', context)