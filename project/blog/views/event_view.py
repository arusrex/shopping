from django.shortcuts import render

def event(request):
    return render(request, 'blog/pages/event.html')