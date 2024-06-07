from django.shortcuts import render
from blog.models import Post

def post(request, slug):
    post = Post.objects.get(slug=slug,)

    context = {
        'post': post,
        'page_title': f'{post.title} - ',
    }

    return render(request, 'blog/pages/post.html', context)