from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from blog.forms import CustomUserChangeForm, ProfileUpdateForm
from blog.models import Profile
from django.contrib.auth.decorators import login_required, user_passes_test

def is_admin(user):
    return user.is_superuser

@login_required
def edit_user(request, user_id):
    profile = get_object_or_404(User, id=user_id)
    form = CustomUserChangeForm(instance=profile)
    form_image = ProfileUpdateForm(instance=profile)

    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=profile)
        form_image = ProfileUpdateForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            new_user = form.save()

            if form_image.is_valid():
                print('Entrou aqui no form_image')
                # image_instance = form_image.save(commit=False)
                # image_instance.user = new_user
                # print(image_instance.user)
                # image_instance.save()
                image_instance = request.FILES.get('profile_image')
                Profile.objects.create(user=new_user, profile_image=image_instance)

                if image_instance:
                    messages.success(request, 'Imagem atualizada com sucesso!')

            messages.success(request, 'Usuário atualizado com sucesso!')
            return redirect('blog:edit_user', user_id=user_id)
        else:
            messages.error(request, 'Algo deu errado ao atualizar seus dados, verifique os campos novamente.')        

    context = {
        'profile': profile,
        'form': form,
        'form_image': form_image,
    }

    return render(request, 'blog/pages/edit_user.html', context)