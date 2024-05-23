from site_setup import models

def site_setup(request):
    setup = models.SiteSetup.objects.order_by('-id').first()

    context = {
        'site_setup': setup,
        }

    return context