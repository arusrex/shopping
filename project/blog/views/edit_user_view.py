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
    user = get_object_or_404(User, id=user_id)
    profile, created = Profile.objects.get_or_create(user=user)

    form = CustomUserChangeForm(instance=user)
    form_image = ProfileUpdateForm(instance=profile)


    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        form_image = ProfileUpdateForm(request.POST, request.FILES, instance=profile)

        # if form.is_valid():
        #     new_user = form.save()

        #     if form_image.is_valid():
        #         new_user.profile_image.profile_image.delete()
        #         image_instance = request.FILES.get('profile_image')
        #         Profile.objects.create(user=new_user, profile_image=image_instance)

            # if form_image.is_valid():
                # image_instance = form_image.save(commit=False)
                # image_instance.user = new_user
                # print(image_instance.user)
                # image_instance.save()

                # if image_instance:
                # messages.success(request, 'Imagem atualizada com sucesso!')

        if form.is_valid() and form_image.is_valid():
            form.save()
            form_image.save()

            if form_image:
                messages.success(request, 'Imagem atualizada com sucesso!')

            messages.success(request, 'Usuário atualizado com sucesso!')
            return redirect('blog:edit_user', user_id=user_id)
        else:
            messages.error(request, 'Algo deu errado ao atualizar seus dados, verifique os campos novamente.')        

    context = {
        'profile': user,
        'form': form,
        'form_image': form_image,
    }

    return render(request, 'blog/pages/edit_user.html', context)

def user_active(request, user_id):
    activated = User.objects.get(id=user_id)

    if request.POST.get('is_active') == 'on':
        activated.is_active = True
        activated.save()
        messages.success(request, 'Usúário ativado')
        return redirect('blog:users')
    else:
        activated.is_active = False
        activated.save()
        messages.error(request, 'Usuário desativado')
        return redirect('blog:users')
    
def user_staff(request, user_id):
    activated = User.objects.get(id=user_id)

    if request.POST.get('is_staff') == 'on':
        activated.is_staff = True
        activated.save()
        messages.success(request, 'Usúário com acesso administrativo')
        return redirect('blog:users')
    else:
        activated.is_staff = False
        activated.save()
        messages.error(request, 'Usuário sem acesso administrativo')
        return redirect('blog:users')
    
def delete_user(request, user_id):
    target = User.objects.get(id=user_id)

    if target:
        target.delete()
        messages.success(request, 'Usuário deletado com sucesso.')
        
        return redirect('blog:users')
