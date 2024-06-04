from site_setup import models
from blog.models import Category
from datetime import datetime, date, time

def site_setup(request):
    setup = models.SiteSetup.objects.order_by('-id').first()
    category = Category.objects.order_by('name')


    hoje = datetime.now().day
    mes_atual = datetime.now().month
    ano_atual = datetime.now().year
    data_atual = date.today()
    hora_atual = datetime.now().time
    context = {
        'site_setup': setup,
        'hoje': hoje,
        'mes_atual': mes_atual,
        'ano_atual': ano_atual,
        'data_atual': data_atual,
        'hora_atual': hora_atual,
        'category': category,
        }

    return context