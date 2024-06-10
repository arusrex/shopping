from django.shortcuts import render
from django.contrib.auth.models import User

def users_views(request):
    users = User.objects.order_by('first_name')

    context = {
        'users': users,
    }

    return render(request, 'blog/pages/users.html', context)