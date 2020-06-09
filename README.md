# Trabalho Final Pyton

- Aluno: Hugo Vinicius Reis Vaz
- Curso: Desenvolvimento Web Full Stack

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

# Imagem do Projeto

- Index: http://localhost:8000/

![alt text](https://github.com/HugoVinicius/python-projeto-final/blob/master/img/index.JPG)

- Lista Recebimento: http://localhost:8000/pagamento/listar

![Screenshot](img/listar_pagamento.JPG)



