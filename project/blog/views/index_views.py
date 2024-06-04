from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import Post, News, Events

def index(request):

    lojas = Post.objects.filter(is_published=True).order_by('-id')
    news = News.objects.filter(is_published=True).order_by('-created_at')[:3]
    events = Events.objects.filter(is_published=True).order_by('-created_at')[:3]

    paginator = Paginator(lojas, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'lojas': lojas,
        'news': news,
        'events': events,
    }

    return render(request, 'blog/pages/index.html', context)