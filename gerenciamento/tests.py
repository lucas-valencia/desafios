from django.test import TestCase
from .models import cliente
from django.core.exceptions import ValidationError

class ClienteModelTest(TestCase):
    
    def setUp(self):
        # Cria um cliente inicial para os testes
        self.cliente = cliente.objects.create(
            nome="ClienteExemplo",
            sobrenome ="SobrenomeExemplo",
            cpf="123.456.789-00",  # CPF válido
            data_nascimento = "1111-01-01",
            gênero = "m",

            cep = "00000000",
            logradouro = "RuaExemplo",
            bairro = "bairoExemplo",
            cidade = "cidadeExemplo",
            estado = "EX",

            telefone="(11) 1111-1111",
            celular="(11) 99999-9999",
            email="cliente@teste.com",
        )

    def test_criacao_cliente(self):
        """Testa se o cliente foi criado corretamente no banco de dados."""
        Cliente = cliente.objects.get(cpf="123.456.789-00")
        self.assertEqual(Cliente.nome, "ClienteExemplo")

    def test_cpf_unico(self):
        """Testa se a aplicação evita a criação de um cliente com CPF duplicado."""
        with self.assertRaises(ValidationError):
            cliente_duplicado = cliente(
            nome="ClienteDuplicado",
            sobrenome ="SobrenomeDuplicado",
            cpf="123.456.789-00",  # CPF válido
            data_nascimento = "2222-02-02",
            gênero = "f",

            cep = "11111111",
            logradouro = "RuaDois",
            bairro = "bairoDois",
            cidade = "cidadeDois",
            estado = "EX",

            telefone="(22) 2222-2222",
            celular="(22) 2222-2222",
            email="clienteduplicado@teste.com",
            )
            cliente_duplicado.full_clean()  # Valida antes de salvar no banco
            cliente_duplicado.save()
