from django.urls import path
from . import views

urlpatterns = [
    # Exemplo de rota temporária, só para confirmar que está funcionando
    path('', views.home, name='home'),
]
