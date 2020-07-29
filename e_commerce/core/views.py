from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm

# Create your views here.
def home_page(request):
    context = {
        'title': 'Página Princípal',
        'context': 'Bem-vindo à página principal'
    }
    return render(request, 'home_page.html', context)

def about_page(request):
    context = {
        'title': 'Página sobre',
        'content': 'Bem-vindo à página sobre'
    }
    return render(request, 'about/view.html', context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        'title': 'Página de contatos',
        'content': 'Bem-vindo à página de contato',
        'form': contact_form
    }
    return render(request, 'contact/view.html', context)


