from django import forms
from .models import Mensagem

class MensagemForm(forms.ModelForm):
    class Meta:
        model = Mensagem
        fields = ['destinatario', 'assunto', 'corpo']
