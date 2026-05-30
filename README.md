# Sistema de Gestão de EPIs 🦺

Este é um projeto base desenvolvido em **Django** e **MySQL** para a gestão, controlE e rastreabilidade de Equipamentos de Proteção Individual (EPIs). O sistema possui controlo de perfis de acesso (Administrador e Operador) e travas automáticas de segurança para o stock.

---

## 🚀 Como Clonar e Configurar o Projeto

Siga os passos abaixo para configurar o projeto no seu ambiente local.

1. Clonar o Repositório
No seu terminal, clone o projeto e aceda à pasta:
```bash
git clone <https://github.com/joaorupp/prova-saep>
cd nome-da-pasta-do-projeto

2. Criar e Ativar o Ambiente Virtual (.venv)
É necessário criar um ambiente isolado para instalar as dependências do Python:
python -m venv .venv
.venv\Scripts\activate

3. Instalar as Dependências
Com o ambiente virtual ativado, instale o Django e o conector do MySQL:
pip install django mysqlclient

4. Configurar o Banco de Dados (MySQL)
    Abra o seu MySQL Workbench (ou terminal do MySQL).

    Certifique-se de que possui um banco de dados criado com o nome configurado no projeto (ex: epi_db):

    CREATE DATABASE epi_db;

5. Executar as Migrações
Gere as tabelas estruturais no seu banco de dados limpo na ordem correta exigida pelo Django:
python manage.py makemigrations gestao
python manage.py migrate

6. Popular o Banco de Dados Automaticamente (Opcional)
Para não precisar de cadastrar tudo manualmente para os testes, execute o script de carga inicial para criar utilizadores, colaboradores e EPIs de teste:

python seed.py