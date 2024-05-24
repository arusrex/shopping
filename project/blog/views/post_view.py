from django.shortcuts import render

def post_view(request):
    return render(request, 'blog:post_view')