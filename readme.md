<h1 align="center"> Sistema Cadastro Pessoas Físicas Python + Django </h1>

<p align="center">
<img loading="lazy" src="http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge"/>
</p>

<p>
Sistema de cadastro e consulta de clientes, conforme solicitado em desafio "hands on".
</p>

<hr>

### Requisitos aplicados

- [x] Ser aplicação WEB
- [x] Contemplar CRUD
- [ ] Banco de dados em memória (H2 ou outros)
- [x] Verificação para evitar cadastros duplicados (CPF como referência)
- [ ] FrontEnd (Opcional)
- [x] Testes unitários (Opicional)

# 📁 Acesso ao projeto

**Apenas clone o repositório GIT**

# 🛠️ Abrir e rodar o projeto

**Instale um gerenciador de pacotes e ambientes virtuais, como Anaconda**

**Via CMD, vá até a pasta "desafios"**

**Pelo prompt, crie um ambiente virtual e instale nele o python**

**>conda create --name nome_do_ambiente python=versão**

**Ative o ambiente virtual criado**

**>conda activate nome_do_ambiente**

**Instale o django**

**>pip install django**

**Dentro da pasta do projeto "desafios":**

**>python manage.py runserver**

**Pelo navegador, acesse "localhost"**

# :hammer: Funcionalidades do projeto

- `Cadastro`: Cadastro via formulário de um cliente por vez
- `Consulta`: Consulta e pesquisa através do nome do cliente
- `Edição`: Edição de usuários existentes
- `Exclusão`: Exclusão de usuários cadastrados