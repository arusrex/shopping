from django.shortcuts import render, redirect
from blog.models import News, ImageNew
from blog.forms import CommentsNewsForm, AddNewsForm, AddImagesNewsForm, EditNewsForm
from django.core.paginator import Paginator
from django.contrib import messages

PER_PAGE = 5
PER_PAGE_ADMIN = 20


def new(request, slug):
    news = News.objects.get(slug=slug)
    comments = news.comments.all().order_by('-created_at') # type: ignore
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentsNewsForm(data=request.POST)
        if comment_form.is_valid(): # type: ignore
            new_comment = comment_form.save(commit=False) # type: ignore
            new_comment.new = news
            new_comment.author = request.user
            new_comment.save()
            return redirect('blog:new', slug=news.slug)
    else:
        comment_form = CommentsNewsForm()
                
        paginator = Paginator(comments, PER_PAGE) # type: ignore
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    context = {
        'new': news,
        'page_title': f'{news.title} - ',
        'page_obj': page_obj,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
    }

    return render(request, 'blog/pages/new.html', context)

def news(request):
    news = News.objects.order_by('-created_at')
                
    paginator = Paginator(news, PER_PAGE_ADMIN) # type: ignore
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }

    return render(request, 'blog/pages/news.html', context)



def add_news(request):
    form = AddNewsForm()
    form_images = AddImagesNewsForm()
    
    if request.method == 'POST':
        form = AddNewsForm(request.POST, request.FILES)
        form_images = AddImagesNewsForm(request.POST, request.FILES)

        if form.is_valid():
            news = form.save()

            if form_images.is_valid():
                i = 0
                images = request.FILES.getlist('image')
                for file in images:
                    ImageNew.objects.create(new=news, image=file)
                    i += 1
                messages.warning(request, f'{i} imagens salvas.')
            messages.success(request, 'Novidades salva com sucesso')
            return redirect('blog:news')

    context = {
        'form': form,
        'form_images': form_images,
    }

    return render(request, 'blog/pages/add_news.html', context)

def edit_news(request, id):
    news = News.objects.get(id=id)
    form = AddNewsForm(instance=news)
    form_images = AddImagesNewsForm(instance=news)
    
    if request.method == 'POST':
        form = AddNewsForm(request.POST, request.FILES, instance=news)
        form_images = AddImagesNewsForm(request.POST, request.FILES, instance=news)

        if form.is_valid():
            new = form.save()

            if form_images.is_valid():
                i = 0
                images = request.FILES.getlist('image')
                for file in images:
                    ImageNew.objects.create(new=new, image=file)
                    i += 1
                messages.warning(request, f'{i} imagens salvas.')
            messages.success(request, 'Novidades salva com sucesso')
            return redirect('blog:news')

    context = {
        'news': news,
        'form': form,
        'form_images': form_images,
    }

    return render(request, 'blog/pages/edit_news.html', context)

def delete_news(request, id):
    news = News.objects.get(id=id)
    if news:
        news.delete()
        messages.success(request, 'Novidades deletada com sucesso')

        return redirect('blog:news')

def delete_image_news(request, id):
    image = ImageNew.objects.get(id=id)
    news_id = image.new.id #type:ignore
    image.delete()
    messages.success(request, 'Imagem deletada!')

    return redirect('blog:edit_news', id=news_id)

def news_published(request, id):
    news = News.objects.get(id=id)
    if request.POST.get('is_published') == 'on':
        news.is_published = True
        news.save()
        messages.success(request, 'Novidade publicada!')

    else:
        news.is_published = False
        messages.success(request, 'Novidade despublicada!')
        news.save()

    # news.is_published = True if request.POST.get('is_published') == 'on' else False
    

    return redirect('blog:news')