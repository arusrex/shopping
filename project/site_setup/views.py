from django.shortcuts import render
from site_setup.forms import SiteSetupForm
from django.contrib import messages
from site_setup.models import SiteSetup

def site_config(request):
    site_setup_instance = SiteSetup.objects.get()

    if request.method == 'POST':
        form = SiteSetupForm(request.POST, request.FILES, instance=site_setup_instance)

        if form.is_valid():
            form.save()
            messages.success(request, "Configurações atualizadas com sucesso")
    else:
        form = SiteSetupForm(instance=site_setup_instance)

    context = {
        'form': form,
    }

    return render(request, 'blog/pages/site_config.html', context)