from django.shortcuts import render

def new(request):
    return render(request, 'blog/pages/new.html')