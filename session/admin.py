from django.contrib import admin

from session.models import *

# Register your models here.
admin.site.register(Session)
admin.site.register(SessionLog)
admin.site.register(SessionPlayers)

admin.site.register(FriendList)
admin.site.register(Solicitacao)
admin.site.register(JogadoresSessao)
admin.site.register(SolicitacaoJogador)