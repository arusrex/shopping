from django.shortcuts import render, redirect
from blog.models import Post
from blog.forms import NewPost

def post(request, slug):
    post = Post.objects.get(slug=slug,)

    context = {
        'post': post,
        'page_title': f'{post.title} - ',
    }

    return render(request, 'blog/pages/post.html', context)

def new_post(request):
    form = NewPost()
    
    if request.method == 'POST':
        form = NewPost(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:admin_dashboard')

    context = {
        'form': form,
        'page_title': 'Adicionar Loja - ',
    }

    return render(request, 'blog/pages/new_post.html', context)