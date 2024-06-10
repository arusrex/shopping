from django.shortcuts import render, redirect
from blog.models import News
from blog.forms import CommentsNewsForm
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