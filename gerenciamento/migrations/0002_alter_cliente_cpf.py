# Generated by Django 5.1.2 on 2024-10-27 18:54

import cpf_field.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciamento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=cpf_field.models.CPFField(max_length=11, unique=True, verbose_name='cpf'),
        ),
    ]
