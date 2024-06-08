from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from blog.forms import LoginForm

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login efetuado com sucesso, bem vindo!')
                return redirect('blog:index')
            else:
                messages.error(request, 'Usuário ou senha inválidos')
    
    form = LoginForm()

    context = {
        'form': form,
    }

    return render(request, 'blog/pages/login.html', context)

def logout_user(request):
    logout(request)
    messages.success(request, 'Saiu da sua conta!')
    return redirect('blog:index')