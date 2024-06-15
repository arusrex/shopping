from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from blog.models import Post, Category, Tag
from django.views.generic import ListView
from blog.forms import CategoryForm, TagForm
from django.contrib import messages


PER_PAGE = 9

def shops(request):
    lojas = Post.objects.get_published().order_by('-id') # type: ignore

    paginator = Paginator(lojas, PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'page_title': 'Lojas - '
    }

    return render(request, 'blog/pages/shops.html', context)

def admin_shops(request):
    lojas = Post.objects.order_by('-id') # type: ignore

    paginator = Paginator(lojas, PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'page_title': 'Lojas - '
    }

    return render(request, 'blog/pages/admin_shops.html', context)

def new_category(request):
    category = Category.objects.order_by('name')
    form = CategoryForm()

    paginator = Paginator(category, PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Categoria adicionada com sucesso')
            return redirect('blog:new_category')

    context = {
        'form': form,
        'page_obj': page_obj,
    }

    return render(request, 'blog/pages/new_category.html', context)

def delete_category(request, category_id):
    category = Category.objects.get(id=category_id)
    category.delete()
    messages.error(request, 'Categoria apagada com sucesso')
    return redirect('blog:new_category')

def new_tag(request):
    tag = Tag.objects.order_by('name')
    form = TagForm()

    paginator = Paginator(tag, PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.method == 'POST':
        form = TagForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Tag adicionada com sucesso')
            return redirect('blog:new_tag')
    
    context = {
        'form': form,
        'page_obj': page_obj,
    }

    return render(request, 'blog/pages/new_tag.html', context)

def delete_tag(request, tag_id):
    tag = Tag.objects.get(id=tag_id)
    tag.delete()
    messages.error(request, 'Tag apagada com sucesso')
    return redirect('blog:new_tag')


# class ShopsViews(ListView):
#     model = Post
#     template_name = 'blog/pages/shops.html'
#     paginate_by = PER_PAGE
#     context_object_name = 'shops'
#     ordering = '-id'
#     queryset = Post.objects.get_published().order_by('-id') # type: ignore

#     # def get_queryset(self):
#     #     queryset = super().get_queryset()
#     #     queryset = queryset.all()
#     #     return queryset

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)

#         context.update({
#             'page_title': 'Lojas - '
#         })

#         return context

