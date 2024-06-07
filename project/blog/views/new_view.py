from django.shortcuts import render
from blog.models import News

def new(request, slug):
    news = News.objects.get(slug=slug)

    context = {
        'new': news,
        'page_title': f'{news.title} - '
    }

    return render(request, 'blog/pages/new.html', context)