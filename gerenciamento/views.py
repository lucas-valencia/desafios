from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from gerenciamento.forms import CadastroForm
from gerenciamento.models import cliente

# Create your views here.

    # Apresenta index.html que está dentro da pasta gerenciamento/templates
def index(request):

    return render(request, 'index.html')

    # Apresenta cadastro.html que está dentro da pasta gerenciamento/templates
def cadastro(request):
    if request.method == "GET":
        form = CadastroForm()
    else:
        form = CadastroForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.save() #Salva no bando de dados OBS.: Se usar mais de um DB ou um DB em memória, especificar em qual DB salvar com cliente.save(using='NOME_DB')
            form = CadastroForm()  # Reinstancia o formulário vazio após salvar
            return redirect('index')
    
    context = {
        'form': form
    }
    return render(request, 'cadastro.html', context=context)

    # Apresenta consulta.html que está dentro da pasta gerenciamento/templates
def consulta(request):
    q = request.GET.get('q', '')
    if q:
        clientes = cliente.objects.filter(nome__icontains=q)
    else:
        clientes = cliente.objects.all()

    # Passando os campos do modelo
    model_fields = cliente._meta.fields

    context = {
        'clientes': clientes,
        'model_fields': model_fields,  # Adicionando os campos do modelo
    }
    return render(request, 'consulta.html', context)

    # Vinculado ao botão "Editar" em consulta.html
def editar_cliente(request, cliente_id):
    cliente_instancia = get_object_or_404(cliente, id=cliente_id)
    if request.method == "POST":
        form = CadastroForm(request.POST, instance=cliente_instancia)
        if form.is_valid():
            form.save()
            return redirect('consulta')
    else:
        form = CadastroForm(instance=cliente_instancia)

    return render(request, 'cadastro.html', {'form': form})

    # Vinculado ao botão "Excluir" em consulta.html
def apagar_cliente(request, cliente_id):
    cliente_instancia = get_object_or_404(cliente, id=cliente_id)
    if request.method == "POST":
        cliente_instancia.delete()
        return redirect('consulta')
    return render(request, 'confirmar_apagar.html', {'cliente': cliente_instancia})