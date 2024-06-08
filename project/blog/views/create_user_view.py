from django.shortcuts import render, redirect
from django.contrib import messages
from blog.forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test

def is_admin(user):
    return user.is_superuser

def create_user(request):

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário criado com sucesso!')
            return redirect('blog:index')
        else:
            messages.success(request, 'Algo deu errado, verifique os campos necessários!')

    else:
        form = CustomUserCreationForm()

    context = {
        'form': form,
    }

    return render(request, 'blog/pages/create_user.html', context)