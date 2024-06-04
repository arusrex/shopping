from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import Post, News, Events, Category

PER_PAGE = 9

def index(request):

    lojas = Post.objects.get_published().order_by('-id') # type: ignore
    news = News.objects.get_published().order_by('-created_at')[:3] # type: ignore
    events = Events.objects.get_published().order_by('-created_at')[:3] # type: ignore

    paginator = Paginator(lojas, PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'lojas': lojas,
        'news': news,
        'events': events,
    }

    return render(request, 'blog/pages/index.html', context)