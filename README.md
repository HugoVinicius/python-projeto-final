# Trabalho Final Pyton

- Aluno: Hugo Vinicius Reis Vaz
- Curso: Desenvolvimento Web Full Stack

# Imagem do Projeto

- Index: http://localhost:8000/

![alt text](https://github.com/HugoVinicius/python-projeto-final/blob/master/img/index.JPG)

- Lista Pagamento: http://localhost:8000/pagamento/listar

![Screenshot](img/listar_pagamento.JPG)

- Adicionar Pagamento: http://localhost:8000/pagamento/cadastrar

![Screenshot](img/criar_pagamento.JPG)

- Editar Pagamento: http://localhost:8000/pagamento/atualizar/1/

![Screenshot](img/editar_pagamento.JPG)

- Lista Recebimento: http://localhost:8000/recebimento/listar

![Screenshot](img/listar_recebimento.JPG)

- Adicionar Recebimento: http://localhost:8000/recebimento/cadastrar

![Screenshot](img/criar_recebimento.JPG)

- Editar Recebimento: http://localhost:8000/recebimento/atualizar/1/

![Screenshot](img/editar_pagamento.JPG)

- Relatório: http://localhost:8000/relatorio/

![Screenshot](img/relatorio.JPG)

- Fluxo de Caixa: http://localhost:8000/fluxocaixa/

![Screenshot](img/fluxo_caixa.JPG)


# Comandos Básicos

Para criar um novo virtual env:

$ python -m venv DIRETORIO

Para ativar o virtual env:

Windows:

$ DIRETORIO\Scripts\activate.bat

Linux:

$ DIRETORIO/bin/activate

Não esquecer:

1º - Criar projeto: python manage.py startapp nomeprojeto

2º - Registrar a aplicação no arquivo settings.py array INSTALLED_APPS = ['nomeprojeto']

3º - Criar estrutura do banco de dados: python manage.py migrate

4º - Rodar o projeto: python manage.py runserver


- Criando superuser admin: python manage.py createsuperuser
- http://127.0.0.1:8000/admin/


python manage.py makemigrations => Rodar migração

python manage.py migrate



