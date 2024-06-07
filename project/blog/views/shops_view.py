from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import Post
from django.views.generic import ListView

PER_PAGE = 9

class ShopsViews(ListView):
    model = Post
    template_name = 'blog/pages/shops.html'
    paginate_by = PER_PAGE
    context_object_name = 'shops'
    ordering = '-id'
    queryset = Post.objects.get_published().order_by('-id') # type: ignore

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     queryset = queryset.all()
    #     return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({
            'page_title': 'Lojas - '
        })

        return context

# def shops(request):
#     lojas = Post.objects.get_published().order_by('-id') # type: ignore

#     paginator = Paginator(lojas, PER_PAGE)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)

#     context = {
#         'page_obj': page_obj,
#         'lojas': lojas,
#         'page_title': 'Lojas - '
#     }

#     return render(request, 'blog/pages/shops.html', context)