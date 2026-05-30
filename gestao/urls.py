# gestao/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_produtos_view, name='lista_produtos'),
    path('produto/<int:produto_id>/movimentar/', views.registrar_movimentacao_view, name='registrar_movimentacao'),
]