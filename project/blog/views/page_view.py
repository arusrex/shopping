from django.shortcuts import render
from blog.models import Page

def page(request, slug):
    pages = Page.objects.get(slug=slug)

    context = {
        'pages': pages,
    }

    return render(request, 'blog/pages/page.html', context)