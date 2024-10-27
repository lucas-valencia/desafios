from django import forms
from gerenciamento.models import cliente

class CadastroForm(forms.ModelForm):
    class Meta:
        model = cliente
        fields = '__all__'
    # Define os textos de ajuda
    def __init__(self, *args, **kwargs):
        super(CadastroForm, self).__init__(*args, **kwargs)
        placeholders = {
            'nome': 'Digite seu primeiro nome',
            'sobrenome': 'Digite seu sobrenome',
            'cpf': 'Apenas números',
            'data_nascimento': 'DD/MM/AAAA',

            'cep': 'Apenas números',
            'logradouro': 'Nome da Rua, Avenida ou Servidão',
            'bairro': 'Seu bairro',
            'cidade': 'Sua cidade',
            'estado': 'Seu estado',

            'telefone': '(DD) 00000-0000',
            'celular': '(DD) 00000-0000',
            'email': 'exemplo@exemplo.com.br',
        }
        # Define texto-ajuda para cada campo dinamicamente (Tem como melhorar)
        for field_name, placeholder in placeholders.items():
            if field_name in self.fields:
                self.fields[field_name].widget.attrs['placeholder'] = placeholder