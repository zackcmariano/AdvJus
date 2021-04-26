from django.shortcuts import render, redirect
from app.forms import ClientesForm
from app.models import Clientes
from django.core.paginator import Paginator


# Create your views here.
def home(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Clientes.objects.filter(email__icontains=search)

    else:
        data['db'] = Clientes.objects.all()
    return render(request, 'index.html', data)

def cadastro(request):
    data = {}
    data['cadastro'] = ClientesForm
    return render(request, 'cadastro.html', data)

def create(request):
    cadastro = ClientesForm(request.POST or None)
    if cadastro.is_valid():
        cadastro.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = Clientes.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Clientes.objects.get(pk=pk)
    data['cadastro'] = ClientesForm(instance=data['db'])
    return render(request, 'cadastro.html', data)

def update(request, pk):
    data = {}
    data['db'] = Clientes.objects.get(pk=pk)
    cadastro = ClientesForm(request.POST or None, instance=data['db'])
    if cadastro.is_valid():
        cadastro.save()
        return redirect('home')

def delete(request, pk):
    db = Clientes.objects.get(pk=pk)
    db.delete()
    return redirect('home')