from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .forms import ContactForm, LoginForm, RegisterForm
from django.contrib.auth import login, get_user_model, authenticate
from core.models import Product
from django.views.generic import ListView, DetailView

# Create your views here.
def home_page(request):
    context = {
        'title': 'Página Princípal',
        'context': 'Bem-vindo à página principal'
    }
    if request.user.is_authenticated:
        context['premium_content']='você é um usuário Premium'
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

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        'form': form
    }
    print('User logged in')
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            print('Usuário válido')
            return redirect('/')
        else:
            print('Login ou senha inválidos')
    return render(request, 'auth/login.html', context)

User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        new_user = User.objects.create_user(username, email, password)
        print(new_user)
    return render(request, 'auth/register.html', context)


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'products/list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        return context

class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'products/detail.html'
    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        return context
    
    def get_object(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404('Esse produto não existe!')
        return instance

class ProductFeaturedListView(ListView):
    template_name = 'products/list.html'

    def get_queryset(self, *args, **kwargs):
        return Product.objects.featured()
    
class ProductFeaturedDetailView(DetailView):
    queryset = Product.objects.all().featured()
    template_name = 'products/featured-detail.html'