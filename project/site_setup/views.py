from django.shortcuts import render
from site_setup.forms import SiteSetupForm
from django.contrib import messages
from site_setup.models import SiteSetup

def site_config(request):
    form = SiteSetupForm(instance=SiteSetup.objects.get())

    if form.is_valid():
        form.save()
        messages.success(request, "Configurações atualizadas com sucesso")

    context = {
        'form': form,
    }

    return render(request, 'blog/pages/site_config.html', context)