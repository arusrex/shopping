from django.shortcuts import render, redirect
from blog.models import Events
from blog.forms import CommentsEventsForm
from django.core.paginator import Paginator

PER_PAGE = 5

def event(request, slug):
    event = Events.objects.get(slug=slug)
    comments = event.comments.all().order_by('-created_at') #type:ignore
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentsEventsForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.event = event
            new_comment.author = request.user
            new_comment.save()
            return redirect('blog:event', slug=event.slug)
    else:
        comment_form = CommentsEventsForm()

        paginator = Paginator(comments, PER_PAGE) # type: ignore
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
       
    context = {
        'event': event,
        'page_title': f'{event.title} - ',
        'page_obj': page_obj,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
    }

    return render(request, 'blog/pages/event.html', context)