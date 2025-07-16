from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Mensagem
from .forms import MensagemForm

# CAIXA DE ENTRADA (mensagens recebidas)
@login_required
def inbox_view(request):
    mensagens_recebidas = Mensagem.objects.filter(destinatario=request.user)
    return render(request, 'mensagens/inbox.html', {'mensagens': mensagens_recebidas})

# NOVA MENSAGEM
class NovaMensagemView(LoginRequiredMixin, CreateView):
    model = Mensagem
    form_class = MensagemForm
    template_name = 'mensagens/nova_mensagem.html'
    success_url = reverse_lazy('inbox')

    def form_valid(self, form):
        form.instance.remetente = self.request.user
        return super().form_valid(form)

# DETALHE DA MENSAGEM
class MensagemDetalheView(LoginRequiredMixin, DetailView):
    model = Mensagem
    template_name = 'mensagens/mensagem_detalhe.html'
    context_object_name = 'mensagem'

    def get_queryset(self):
        # Garante que só o destinatário veja a mensagem
        return Mensagem.objects.filter(destinatario=self.request.user)

# CAIXA DE SAÍDA (mensagens enviadas)
@login_required
def saida_view(request):
    mensagens_enviadas = Mensagem.objects.filter(remetente=request.user)
    return render(request, 'mensagens/saida.html', {'mensagens': mensagens_enviadas})

# RESPONDER MENSAGEM
class ResponderMensagemView(LoginRequiredMixin, CreateView):
    model = Mensagem
    form_class = MensagemForm
    template_name = 'mensagens/nova_mensagem.html'  # Usa o mesmo template de nova mensagem
    success_url = reverse_lazy('inbox')

    def dispatch(self, request, *args, **kwargs):
        self.mensagem_original = Mensagem.objects.get(pk=kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def get_initial(self):
        return {
            'destinatario': self.mensagem_original.remetente,
            'assunto': f"Re: {self.mensagem_original.assunto}",
        }

    def form_valid(self, form):
        form.instance.remetente = self.request.user
        return super().form_valid(form)