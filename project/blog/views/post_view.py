from django.shortcuts import render, redirect
from blog.models import Post
from blog.forms import NewPost, NewImagesPost

def post(request, slug):
    post = Post.objects.get(slug=slug,)

    context = {
        'post': post,
        'page_title': f'{post.title} - ',
    }

    return render(request, 'blog/pages/post.html', context)

def new_post(request):
    form = NewPost()
    form_images = NewImagesPost()

    if request.method == 'POST':
        form = NewPost(request.POST, request.files['image'])
        if form.is_valid():
            form.save(commit=False)
            for file in request.files['image']:
                file = form_images.save()
            return redirect('blog:admin_dashboard')

    context = {
        'form': form,
        'form_images': form_images,
        'page_title': 'Adicionar Loja - ',
    }

    return render(request, 'blog/pages/new_post.html', context)