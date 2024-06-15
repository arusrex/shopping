from django.shortcuts import render, redirect
from blog.models import User, CommentsEvents, CommentsNews, NewsLetter

def admin_dashboard(request):
    new_users = User.objects.order_by('-id')[:5]
    new_comments = CommentsNews.objects.order_by('-created_at')[:5]
    event_comments = CommentsEvents.objects.order_by('-created_at')[:5]
    news_letters = NewsLetter.objects.order_by('-id')[:5]

    context = {
        'new_users': new_users,
        'new_comments': new_comments,
        'event_comments': event_comments,
        'news_letters': news_letters,
    }

    return render(request, 'blog/partials/_main_dashboard.html', context)