# Blog da Martina 📝

Projeto desenvolvido com Django para o curso de Python da Coderhouse.

## Funcionalidades
- Cadastro e login de usuários
- Envio de mensagens entre usuários
- Caixa de entrada e de saída
- Interface web simples e funcional

## Tecnologias utilizadas
- Python 3.13
- Django 5.2
- HTML5 / CSS3 básico

## Como rodar o projeto localmente

```bash
git clone https://github.com/martinanunesb29/blogmartina.git
cd blogmartina
python -m venv venv
venv\Scripts\activate  # no Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
