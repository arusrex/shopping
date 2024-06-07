from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import Post, News, Events
from django.db.models import Count

PER_PAGE = 9


def index(request):
    shops = Post.objects.get_published().order_by('-id') # type: ignore
    news = News.objects.get_published().annotate(num_comments=Count('comments')).order_by('-created_at')[:3] # type: ignore
    events = Events.objects.get_published().annotate(num_comments=Count('comments')).order_by('-created_at')[:3] # type: ignore

    paginator = Paginator(shops, PER_PAGE) # type: ignore
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'shops': page_obj,
        'news': news,
        'events': events,
    }

    return render(request, 'blog/pages/index.html', context)