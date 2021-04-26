from django import forms
from django.forms import ModelForm
from app.models import Clientes

class ClientesForm(ModelForm):
    class Meta:
        model = Clientes
        fields = ['nome', 'rg', 'cpf', 'nasc', 'sexo', 'ddd', 'telefone', 'email']

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome completo'}),
            'rg': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite - RG'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite - CPF'}),
            'nasc': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Data de Nascimento'}),
            'sexo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sexo'}),
            'ddd': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'DDD'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefone'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu Melhor E-mail'}),
        }

