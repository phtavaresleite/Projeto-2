from django.shortcuts import render
from django.contrib import messages
from .forms import ContatoForm, ProdutoModelForm
from .models import Produto

from .auth import LoginForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

# Create your views here.
def index(request):
    produtos = Produto.objects.all()
    context = {
        'produtos': produtos
    }
    return render(request, 'index.html', context)

def contato(request):
    form = ContatoForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.send_mail()
            messages.success(request, 'Mensagem enviada com sucesso!')
            print(contato)
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar mensagem!')

    context = {
        'form': form
    }
    return render(request, 'contato.html', context)


def produtos(request):
    if request.method == 'POST':
        form = ProdutoModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            messages.success(request, 'Produto cadastrado com sucesso!')
            form = ProdutoModelForm()
        else:
            messages.error(request, 'Erro ao cadastrar produto!')
    else:
        form = ProdutoModelForm()
        
    context = {
        'form': form
    }
    return render(request, 'produtos.html', context)

class LoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'