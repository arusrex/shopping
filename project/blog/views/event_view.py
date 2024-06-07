from django.shortcuts import render
from blog.models import Events

def event(request, slug):
    event = Events.objects.get(slug=slug)


    context = {
        'event': event,
        'page_title': f'{event.title} - '
    }

    return render(request, 'blog/pages/event.html', context)