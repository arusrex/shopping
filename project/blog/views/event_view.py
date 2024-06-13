from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Events, ImageEvent
from blog.forms import CommentsEventsForm, AddEventsForm, EditEventsForm, AddImagesEventsForm
from django.core.paginator import Paginator
from django.contrib import messages

PER_PAGE = 5
PER_PAGE_ADMIN = 20

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

def events(request):
    events = Events.objects.order_by('-created_at')

    paginator = Paginator(events, PER_PAGE_ADMIN) # type: ignore
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
       
    context = {
        'page_obj': page_obj,
    }

    return render(request, 'blog/pages/events.html', context)

def add_event(request):
    form = AddEventsForm()
    form_images = AddImagesEventsForm()

    if request.method == 'POST':
        form = AddEventsForm(request.POST, request.FILES)
        form_images = AddImagesEventsForm(request.POST, request.FILES)

        if form.is_valid():
            event_ = form.save()

            if form_images.is_valid():
                i = 0 
                images = request.FILES.getlist('image')
                for file in images:
                    ImageEvent.objects.create(event=event_, image=file)
                    i += 1
                messages.warning(request, f'{i} imagens salvas com sucesso')
            messages.success(request, 'Evento salvo com sucesso')
            return redirect('blog:events')

    context = {
        'form': form,
        'form_images': form_images,
    }

    return render(request, 'blog/pages/add_events.html', context)


def edit_event(request, id):
    event_ = Events.objects.get(id=id)
    form = EditEventsForm(instance=event_)
    form_images = AddImagesEventsForm(instance=event_)

    if request.method == 'POST':
        form = EditEventsForm(request.POST, request.FILES, instance=event_)
        form_images = AddImagesEventsForm(request.POST, request.FILES, instance=event_)

        if form.is_valid():
            new_event = form.save()

            if form_images.is_valid():
                i = 0
                images = request.FILES.getlist('image')
                for file in images:
                    ImageEvent.objects.create(event=new_event, image=file)
                    i += 1
                messages.warning(request, f'{i} imagens salvas.')
            messages.success(request, 'Evento atualizado com sucesso.')
            return redirect('blog:edit_event', id=id)

    context = {
        'events': event_,
        'form': form,
        'form_images': form_images,
    }

    return render(request, 'blog/pages/edit_events.html', context)


def delete_event(request, id):
    event_ = get_object_or_404(Events, id=id)
    if event_:
        event_.delete()
        messages.success(request, 'Evento excluído com sucesso.')
    return redirect('blog:events')

def delete_image_event(request, id):
    image = ImageEvent.objects.get(id=id)
    event_id = image.event.id #type:ignore
    if image:
        image.delete()
    return redirect('blog:edit_event', id=event_id)

def event_published(request, id):
    event_ = Events.objects.get(id=id)
    if request.POST.get('is_published') == 'on':
        event_.is_published = True
        event_.save()
        messages.success(request, 'Evento publicado.')
    else:
        event_.is_published = False
        event_.save()
        messages.warning(request, 'Evento despublicado')

    return redirect('blog:events')