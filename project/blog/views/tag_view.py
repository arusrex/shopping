from django.shortcuts import render
from blog.models import Post
from django.core.paginator import Paginator

PER_PAGE = 9

def tag(request, slug):

    shops = Post.objects.get_published().filter(tags__slug=slug).order_by('id') # type: ignore

    paginator = Paginator(shops, PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }

    return render(request, 'blog/pages/shops.html', context)