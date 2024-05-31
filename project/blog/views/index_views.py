from django.shortcuts import render
from django.core.paginator import Paginator

def index(request):

    # item_list = Item.objects.all()

    # paginator = Paginator(iteem_list, 9)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)

    # context = {
    #     'page_obj': page_obj,
    # }

    return render(request, 'blog/pages/index.html')