from django.shortcuts import render, redirect
from blog.models import News
from blog.forms import CommentsNewsForm

def new(request, slug):
    news = News.objects.get(slug=slug)
    comments = news.comments.all().order_by('-created_at')[:10] # type: ignore
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentsNewsForm(data=request.POST)
        if comment_form.is_valid(): # type: ignore
            new_comment = comment_form.save(commit=False) # type: ignore
            new_comment.new = news
            new_comment.author = request.user
            new_comment.save()
            return redirect('blog:new', slug=news.slug)
    else:
        comment_form = CommentsNewsForm()
            

    context = {
        'new': news,
        'page_title': f'{news.title} - ',
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
    }

    return render(request, 'blog/pages/new.html', context)