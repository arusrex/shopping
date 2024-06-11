from django.shortcuts import render, redirect
from blog.models import Post
from blog.forms import NewPost, NewImagesPost
from blog.models import ImagesPost
from django.contrib import messages
from django.utils.text import slugify


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
        form = NewPost(request.POST, request.FILES)
        form_images = NewImagesPost(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.slug = slugify(post.title)
            post.save()

            if form_images.is_valid():
                i = 0
                for file in request.FILES.getlist('image'):
                    ImagesPost.objects.create(post=post, image=file)
                    # messages.warning(request, f'Adicionando imagem {i}')
                    i += 1
                messages.warning(request, f'Foram adicionadas {i} imagens')

            messages.success(request, 'Loja cadastrada com sucesso!')
            return redirect('blog:admin_dashboard')


    context = {
        'form': form,
        'form_images': form_images,
        'page_title': 'Adicionar Loja - ',
    }

    return render(request, 'blog/pages/new_post.html', context)