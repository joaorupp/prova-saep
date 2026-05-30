from django.contrib import admin
from .models import Produto, Movimentacao

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'quantidade_estoque', 'data_cadastro')
    search_fields = ('nome',)

@admin.register(Movimentacao)
class MovimentacaoAdmin(admin.ModelAdmin):
    list_display = ('produto', 'tipo', 'quantidade', 'data_hora', 'usuario_responsavel')
    list_filter = ('tipo', 'data_hora')