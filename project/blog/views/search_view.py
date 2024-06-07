from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import Post, News, Events
from django.db.models import Q

PER_PAGE = 9

def search(request):
    search_value = request.GET.get('search-all', '').strip()
    lojas = Post.objects.get_published().order_by('-id') # type: ignore

    if search_value:
        lojas = (Post.objects.get_published() # type: ignore
            .filter(
                Q(title__icontains=search_value) |
                Q(short_description__icontains=search_value) |
                Q(description__icontains=search_value) |
                Q(number__icontains=search_value)
            )[:PER_PAGE]
        )

    paginator = Paginator(lojas, PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'shops': lojas,
        'search_value': search_value,
    }

    return render(request, 'blog/pages/shops.html', context)