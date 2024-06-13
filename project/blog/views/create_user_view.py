from django.shortcuts import render, redirect
from django.contrib import messages
from blog.forms import CustomUserCreationForm, ImageUserForm
from blog.models import ImageUser
from django.contrib.auth.decorators import login_required, user_passes_test

def is_admin(user):
    return user.is_superuser

def create_user(request):

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        form_image = ImageUserForm(request.POST, request.FILES)
        if form.is_valid():
            new_user = form.save()

            if form_image.is_valid():
                image = request.FILES.get('image')
                new_image = ImageUser.objects.create(user=new_user, image=image)
                new_image.save()
                messages.success(request, 'Imagem de perfil salva com sucesso')

            messages.success(request, 'Usuário criado com sucesso!')
            return redirect('blog:index')
        else:
            messages.error(request, 'Algo deu errado, verifique os campos necessários!')

    else:
        form = CustomUserCreationForm()
        form_image = ImageUserForm()

    context = {
        'form': form,
        'form_image': form_image,
    }

    return render(request, 'blog/pages/create_user.html', context)