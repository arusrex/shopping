from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from blog.forms import CustomPasswordChangeForm
from django.contrib.auth.decorators import login_required

def is_admin(user):
    return user.is_superuser

@login_required
def change_password(request, user_id):

    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = CustomPasswordChangeForm(user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Senha atualizada com sucesso!')
            return redirect('blog:change_password', user_id=user_id)
        else:
            print(form.errors)
            messages.error(request, 'Algo deu errado ao alterar sua senha, verifique os campos e tente novamente.')
    else:
        form = CustomPasswordChangeForm(user)

    context = {
        'form': form,
    }

    return render(request, 'blog/pages/change_password.html', context)