from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),         # páginas do blog (home, posts etc.)
    path('accounts/', include('accounts.urls')),  # login, registro, perfil
    path('mensagens/', include('mensagens.urls')),  # mensagens entre usuários
    path('', include('django.contrib.auth.urls')),  # <- Isso habilita login, logout, password_reset etc.
]

# arquivos de mídia
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

