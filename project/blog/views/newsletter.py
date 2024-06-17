from blog.forms import NewsLetterForm
from django.contrib import messages
from django.shortcuts import redirect, render
from blog.models import NewsLetter
from django.contrib import messages
from django.core.paginator import Paginator

def subs(request):
    data = NewsLetter.objects.order_by('-id')
    
    paginator = Paginator(data, 20) # type: ignore
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }

    return render(request, 'blog/partials/_newsletters.html', context)

def newsletter(request):
    if request.method == 'POST':
        subscribe = NewsLetterForm(request.POST)
        if subscribe.is_valid():
            subscribe.save()
            messages.success(request, 'Inscrito com sucesso para receber os destaques, eventos  novidades !')
            return redirect('blog:index')
        
def delete_newsletter(request, newsletter_id):
    news_letter = NewsLetter.objects.filter(id=newsletter_id)
    if news_letter:
        news_letter.delete()
        messages.success(request, 'Inscrição apagada com sucesso')
    else:
        messages.error(request, 'Erro ao apagar')

    return redirect('blog:admin_dashboard')
