from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from blog.forms import CustomPasswordChangeForm
from django.contrib.auth.decorators import login_required, user_passes_test

def is_admin(user):
    return user.is_superuser

@login_required
@user_passes_test(is_admin)
def change_password(request, user_id):

    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = CustomPasswordChangeForm(user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Senha atualizada com sucesso!')
            return redirect('blog:change_passord', user_id=user_id)
    
    form = CustomPasswordChangeForm(user)

    context = {
        'form': form,
    }

    return render(request, 'blog/pages/change_password.html', context)