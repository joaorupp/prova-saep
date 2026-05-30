import os
import django

# 1. CONFIGURAÇÃO DO AMBIENTE DJANGO (Conforme a sua estrutura de pastas)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'almoxarifado_project.settings')
django.setup()

# 2. IMPORTAÇÃO DOS MODELOS DO PROJETO
from django.contrib.auth.models import User
from gestao.models import Produto, Movimentacao

def popular_banco_prova():
    print("⏳ A iniciar a carga de dados oficial para a prova do Almoxarifado...")

    # --- 1. GESTÃO DE USUÁRIOS, PERFIS E SEGURANÇA (Entrega 3 da Prova) ---
    # Criar Administrador do Sistema (Pode Consultar, Inserir, Atualizar e Deletar)
    admin_user, criado_admin = User.objects.get_or_create(
        username='admin',
        defaults={
            'email': 'admin@almoxarifado.com',
            'is_staff': True,
            'is_superuser': True  # Concede privilégios totais de Administrador
        }
    )
    if criado_admin:
        admin_user.set_password('admin123')
        admin_user.save()
        print("✅ Usuário 'admin' (Administrador do Sistema) criado. (Senha: admin123)")

    # Criar Operador de Almoxarifado (Apenas Consultar, Inserir e Atualizar)
    operador_user, criado_operador = User.objects.get_or_create(
        username='operador',
        defaults={
            'email': 'operador@almoxarifado.com',
            'is_staff': True,  # Permite fazer login no painel caso necessário
            'is_superuser': False  # Restrito, não possui privilégios de Admin
        }
    )
    if criado_operador:
        operador_user.set_password('op123')
        operador_user.save()
        print("✅ Usuário 'operador' (Operador de Almoxarifado) criado. (Senha: op123)")


    # --- 2. OPERAÇÕES E FUNCIONALIDADES DE ESTOQUE (Entrega 4 da Prova) ---
    # Cadastrar produtos iniciais com saldos específicos para os testes de Critério de Aceite
    produtos_dados = [
        {
            "nome": "Detergente Industrial 5L", 
            "descricao": "Insumo base - Material de limpeza concentrado", 
            "quantidade_estoque": 15
        },
        {
            "nome": "Desinfetante Hospitalar", 
            "descricao": "Insumo de alta eficiência para desinfecção", 
            "quantidade_estoque": 8
        },
        {
            "nome": "Luva de Látex Descartável", 
            "descricao": "Equipamento de proteção para manuseamento de químicos", 
            "quantidade_estoque": 150
        },
        {
            "nome": "Pulverizador Plástico 1L", 
            "descricao": "Frasco aplicador para diluição de insumos", 
            "quantidade_estoque": 3  # Stock baixo de propósito para testar o bloqueio de saída!
        },
    ]

    produtos_criados = {}

    for p_info in produtos_dados:
        produto, criado_prod = Produto.objects.get_or_create(
            nome=p_info["nome"],
            defaults={
                "descricao": p_info["descricao"],
                "quantidade_estoque": p_info["quantidade_estoque"]
            }
        )
        produtos_criados[p_info["nome"]] = produto
        if criado_prod:
            print(f"📦 Produto Base cadastrado: {produto.nome} (Stock inicial: {produto.quantidade_estoque})")


    # --- 3. REGISTO DE MOVIMENTAÇÕES INICIAIS (Rastreabilidade) ---
    # Gravar as primeiras movimentações vinculando a data/hora automática e o utilizador responsável
    movimentacoes_dados = [
        {
            "produto_nome": "Detergente Industrial 5L", 
            "tipo": "ENTRADA", 
            "quantidade": 10, 
            "user": admin_user
        },
        {
            "produto_nome": "Luva de Látex Descartável", 
            "tipo": "SAIDA", 
            "quantidade": 20, 
            "user": operador_user
        },
    ]

    for m_info in movimentacoes_dados:
        prod_obj = produtos_criados.get(m_info["produto_nome"])
        
        if prod_obj:
            Movimentacao.objects.create(
                produto=prod_obj,
                tipo=m_info["tipo"],
                quantidade=m_info["quantidade"],
                usuario_responsavel=m_info["user"]
            )
            print(f"📋 Movimentação Histórica: {m_info['tipo']} de {m_info['quantidade']}x {m_info['produto_nome']} por '{m_info['user'].username}'")

    print("\n🎉 Banco de dados povoado com sucesso! Pronto para a execução dos 3 cenários de testes.")

if __name__ == '__main__':
    popular_banco_prova()