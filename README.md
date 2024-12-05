# 🚀 Projeto Django

## Visão Geral

Este é um projeto Django que visa criar uma aplicação web para gerenciar produtos e contatos.

## ✨ Funcionalidades

- Listagem de produtos
- Cadastro de produtos (requer autenticação)
- Envio de mensagens de contato
- Autenticação de usuários

## 🛠️ Requisitos

### Ambiente
- Python 3.12
- Django 5.1.3

### Bibliotecas Adicionais
- Bootstrap 5
- StdImage

## 🚀 Instalação

### Passos para Configuração

1. Clone o repositório:
   ```bash
   git clone https://github.com/phtavaresleite/Projeto-Cadastro_de_Produtos
   ```

2. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   ```

3. Ative o ambiente virtual:
   - Linux/Mac:
     ```bash
     source venv/bin/activate
     ```
   - Windows:
     ```bash
     venv\Scripts\activate
     ```

4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

5. Execute as migrações:
   ```bash
   python manage.py migrate
   ```

## 🖥️ Execução

Execute o servidor de desenvolvimento:
```bash
python manage.py runserver
```

Acesse a aplicação em: `http://localhost:8000`

## 🔐 Autenticação

- Para acessar a página de produtos, é necessário estar autenticado.
- A autenticação é feita usando o formulário de login em `login.html`.

## 📬 Contato

- Para enviar uma mensagem de contato, preencha o formulário em `contato.html`.

## 📋 Produtos

- A lista de produtos está disponível em `index.html`.
- O cadastro de produtos é feito em `produtos.html` e requer autenticação.

## ⚠️ Observações

Este é um projeto em desenvolvimento e pode conter erros ou funcionalidades incompletas.

### Contribuições

Para contribuir com o projeto:
1. Faça um fork do repositório
2. Crie uma branch para sua feature
3. Commit suas alterações
4. Envie um pull request