from blog.forms import NewsLetterForm
from django.contrib import messages
from django.shortcuts import redirect

def newsletter(request):
    subscribe = NewsLetterForm()

    if request.method == 'POST':
        subscribe = NewsLetterForm(request.POST)
        if subscribe.is_valid():
            subscribe.save()
            messages.success(request, 'Inscrito com sucesso para receber os destaques, eventos  novidades !')
            return redirect('blog:index')

    context = {
        'subscribe': subscribe,
    }

    return context