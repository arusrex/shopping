from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import Post
from blog.forms.form_category_filter import CategoryFilter

PER_PAGE = 9

def shops(request):
    form = CategoryFilter(request.GET)
    lojas = Post.objects.get_published().order_by('-id') # type: ignore

    if form.is_valid():
        category = form.cleaned_data.get('category')
        if category:
            lojas = Post.objects.get_published().filter(category=category).order_by('-id') # type: ignore

    paginator = Paginator(lojas, PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'lojas': lojas,
    }

    return render(request, 'blog/pages/shops.html', context)