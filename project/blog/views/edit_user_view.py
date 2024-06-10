from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from blog.forms import CustomUserChangeForm
from django.contrib.auth.decorators import login_required, user_passes_test

def is_admin(user):
    return user.is_superuser

@login_required
def edit_user(request, user_id):

    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário atualizado com sucesso!')
            return redirect('blog:edit_user', user_id=user_id)
        else:
            messages.error(request, 'Algo deu errado ao atualizar seus dados, verifique os campos novamente.')
    else:
        form = CustomUserChangeForm(instance=user)
    
    context = {
        'form': form,
    }

    return render(request, 'blog/pages/edit_user.html', context)