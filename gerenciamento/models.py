from django.apps import AppConfig
from django.db import models
from django.urls import reverse
from cpf_field.models import CPFField #biblioteca validador CPF
from django import forms
from django.core.management import call_command

# MODELOS

# Tentativa de aplicar bando de dados em memória \/
"""
class MemoryDbOnlyConfig(AppConfig):
    name = 'memory_db_only'

    def ready(self):
        call_command('migrate',
                     app_label='gerenciamento',
                     verbosity=1,
                     interactive=False,
                     database='memory')
        return self.name
"""
 # Used to generate URLs by reversing the URL patterns

# Generos cadastrados para o objeto gênero da classe cliente
GENEROS = (
    ('m', 'Masculino'),
    ('f', 'Feminino'),
    ('n', 'Não Informar')
)

# Classe principal | Cria a tabela "gerenciamento_cliente"
class cliente(models.Model):
    nome = models.CharField(max_length=200)
    sobrenome = models.CharField(max_length=200)
    cpf = CPFField('cpf')
    data_nascimento = models.DateField(blank=True, null=True)
    gênero = models.CharField(max_length=1, choices=GENEROS)

    cep = models.CharField(max_length=8)
    logradouro = models.CharField(max_length=200, blank=True)
    bairro = models.CharField(max_length=200, blank=True)
    cidade = models.CharField(max_length=100, blank=True)
    estado = models.CharField(max_length=2, blank=True)

    telefone = models.CharField(max_length=15, blank=True, null=True)
    celular = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)


    def __str__(self):
        return self.nome #Objeto "nome" aparecerá como identificador em uma query.