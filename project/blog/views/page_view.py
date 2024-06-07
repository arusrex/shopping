from django.shortcuts import render
from blog.models import Page

def page(request, slug):
    pages = Page.objects.filter(slug=slug).filter(is_published=True).first()
    page_title = f'{pages.title} - ' # type: ignore

    context = {
        'pages': pages,
        "page_title": page_title,
    }

    return render(request, 'blog/pages/page.html', context)