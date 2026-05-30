# gestao/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto, Movimentacao

def lista_produtos_view(request):
    # Procura todos os produtos cadastrados no banco
    produtos = Produto.objects.all()
    # Envia a lista para a página lista.html
    return render(request, 'gestao/lista.html', {'produtos': produtos})

def registrar_movimentacao_view(request, produto_id):
    # Busca o produto específico pelo ID ou dá erro 404 se não existir
    produto = get_object_or_404(Produto, id=produto_id)
    erro = None

    if request.method == "POST":
        tipo = request.POST.get('tipo')
        quantidade = int(request.POST.get('quantidade'))

        if quantidade <= 0:
            print("A quantidade deve ser maior que 0")
        elif quantidade > estoque:
            print("Quantidade inserida é maior que o estoque disponível!")
        else:
            return quantidade = int(request.POST.get('quantidade'))
        # --- ESTADO INICIAL PARA OS ALUNOS ---
        # Aqui o sistema simplesmente aceita a operação sem validar nada.
        # Na prova, o aluno terá de modificar este trecho!
        
        if tipo == 'ENTRADA':
            produto.quantidade_estoque += quantidade
        elif tipo == 'SAIDA':
            produto.quantidade_estoque -= quantidade
        
        produto.save()

        # Regista o histórico da movimentação
        Movimentacao.objects.create(
            produto=produto,
            tipo=tipo,
            quantidade=quantidade,
            usuario_responsavel=request.user # Usa o utilizador que fez login
        )
        
        return redirect('lista_produtos')

    return render(request, 'gestao/movimentacao.html', {'produto': produto, 'erro': erro})