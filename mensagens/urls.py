from django.urls import path
from .views import (
    inbox_view,
    NovaMensagemView,
    MensagemDetalheView,
    saida_view,
    ResponderMensagemView
)

urlpatterns = [
    path('', inbox_view, name='inbox'),
    path('nova/', NovaMensagemView.as_view(), name='nova_mensagem'),
    path('<int:pk>/', MensagemDetalheView.as_view(), name='mensagem_detalhe'),
    path('saida/', saida_view, name='caixa_saida'),
    path('responder/<int:pk>/', ResponderMensagemView.as_view(), name='responder_mensagem'),
]
