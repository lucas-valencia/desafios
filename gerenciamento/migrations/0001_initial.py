# Generated by Django 5.1.2 on 2024-10-27 18:13

import cpf_field.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('sobrenome', models.CharField(max_length=200)),
                ('cpf', cpf_field.models.CPFField(max_length=14, verbose_name='cpf')),
                ('data_nascimento', models.DateField(blank=True, null=True)),
                ('gênero', models.CharField(choices=[('m', 'Masculino'), ('f', 'Feminino'), ('n', 'Não Informar')], max_length=1)),
                ('cep', models.CharField(max_length=8)),
                ('logradouro', models.CharField(blank=True, max_length=200)),
                ('bairro', models.CharField(blank=True, max_length=200)),
                ('cidade', models.CharField(blank=True, max_length=100)),
                ('estado', models.CharField(blank=True, max_length=2)),
                ('telefone', models.CharField(blank=True, max_length=15, null=True)),
                ('celular', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
    ]
