from django.shortcuts import render, redirect
from blog.models import Post
from blog.forms import NewPost, NewImagesPost, EditPost, EditImagesPost
from blog.models import ImagesPost
from django.contrib import messages
from django.utils.text import slugify
from django.views.decorators.http import require_POST

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


def edit_post(request, id):
    post = Post.objects.get(id=id)
    form = EditPost(instance=post)
    form_images = EditImagesPost(instance=post)

    if request.method == 'POST':
        form = EditPost(request.POST, request.FILES, instance=post)
        form_images = EditImagesPost(request.POST, request.FILES, instance=post)

        if form.is_valid():
            post_update = form.save()

            if form_images.is_valid():
                i = 0
                for file in request.FILES.getlist('image'):
                    ImagesPost.objects.create(post=post_update, image=file)
                    i += 1
                messages.warning(request, f'Foram adicionadas {i} imagens')

            messages.success(request, 'Loja atualizada com sucesso!')
            return redirect('blog:edit_post', id=post.id) #type:ignore

    context = {
        'post': post,
        'form': form,
        'form_images': form_images,
        'page_title': 'Editar Loja - ',
    }
    return render(request, 'blog/pages/edit_post.html', context)


def delete_post(request, id):
    post = Post.objects.filter(id=id)
    post.delete()
    messages.warning(request, 'Loja excluída com sucesso!')
    return redirect('blog:admin_dashboard')

def delete_image_post(request, id):

    image = ImagesPost.objects.get(id=id)
    post_id = image.post.id # type:ignore
    image.delete()
    messages.warning(request, 'Imagem excluída com sucesso!')

    return redirect('blog:edit_post', id=post_id)

@require_POST
def shop_published(request, id):
    post = Post.objects.get(id=id)
    post.is_published = True if request.POST.get('is_published') == 'on' else False
    post.save()
    return redirect('blog:admin_shops')



