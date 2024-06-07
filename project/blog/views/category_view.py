from django.shortcuts import render
from blog.models import Post
from django.core.paginator import Paginator

PER_PAGE = 9

def category(request, slug):
    shops = Post.objects.get_published().filter(category__slug=slug).order_by('id') # type: ignore
    for i in shops:
        category = f'{i.category.name} - '

    paginator = Paginator(shops, PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'page_title': category,
    }

    return render(request, 'blog/pages/shops.html', context)