from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from blog.forms import CustomUserChangeForm, ImageUserForm
from blog.models import ImageUser
from django.contrib.auth.decorators import login_required, user_passes_test

def is_admin(user):
    return user.is_superuser

@login_required
def edit_user(request, user_id):

    user = get_object_or_404(User, id=user_id)
    try:
        image_user = ImageUser.objects.get(user=user)
    except ImageUser.DoesNotExist:
        image_user = None

    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        form_image = ImageUserForm(request.POST, request.FILES, instance=image_user)

        if form.is_valid() and form_image.is_valid():
            form.save()
            form_image.save()
            messages.success(request, 'Usuário atualizado com sucesso!')
            return redirect('blog:edit_user', user_id=user_id)
        else:
            messages.error(request, 'Algo deu errado ao atualizar seus dados, verifique os campos novamente.')
    else:
        form = CustomUserChangeForm(instance=user)
        form_image = ImageUserForm(instance=image_user) 

    context = {
        'user_image': user,
        'form': form,
        'form_image': form_image,
    }

    return render(request, 'blog/pages/edit_user.html', context)