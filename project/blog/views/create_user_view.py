from django.shortcuts import render, redirect
from django.contrib import messages
from blog.forms import CustomUserCreationForm, ProfileUpdateForm
from blog.models import Profile
from django.contrib.auth.decorators import login_required, user_passes_test

def is_admin(user):
    return user.is_superuser

def create_user(request):

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        form_image = ProfileUpdateForm(request.POST, request.FILES)

        if form.is_valid():
            new_user = form.save()

            if form_image.is_valid():
                image = request.FILES.get('profile_image')
                Profile.objects.create(user=new_user, profile_image=image)
                messages.success(request, 'Imagem de perfil salva com sucesso')

            messages.success(request, 'Usuário criado com sucesso!')
            return redirect('blog:index')
        else:
            messages.error(request, 'Algo deu errado, verifique os campos necessários!')

    else:
        form = CustomUserCreationForm()
        form_image = ProfileUpdateForm()

    context = {
        'form': form,
        'form_image': form_image,
    }

    return render(request, 'blog/pages/create_user.html', context)