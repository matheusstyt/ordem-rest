from rest_framework import routers
from django.contrib import admin
from django.urls import include, path

from api.views.token import GetToken, LogoutView
from api.views.session import *
from api.views.personagem import *
from api.views.user import *
from rest_framework.authtoken import views
router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
#router.register(r'registrar', RegistrarView.as_view(), basename='user')
router.register(r'contact', FriendListViewSet, basename='FriendList')
router.register(r'ask', SolicitacaoContatoViewSet, basename='solicitacaocontato')
router.register(r'session', SessionViewSet, basename='session')
router.register(r'acessorios', AcessoriosViewSet, basename='acessorios')
router.register(r'rituais', RituaisViewSet, basename='rituais')

# ROTAS DE SESSÕES / PAINEL

router.register(r'askplayer', SolicitacaoJogadorViewSet, basename='JogadoresSessao')
router.register(r'players', JogadoresSessaoViewSet, basename='JogadoresSessao')

router.register(r'atributo', AtributoViewSet, basename='atributo')
router.register(r'atributos', AtributosViewSet, basename='atributos')

router.register(r'pericia', PericiaViewSet, basename='pericia')
router.register(r'pericias', PericiasViewSet, basename='pericias')

router.register(r'resistencia', ResistenciaViewSet, basename='resistencia')
router.register(r'resistencias', ResistenciasViewSet, basename='resistencias')

router.register(r'armamentosSession', ArmamentosViewSet, basename='armamentos')
router.register(r'armamentoSession', ArmamentoViewSet, basename='armamento')

router.register(r'acessoriosSession', AcessoriosViewSet, basename='acessorios')
router.register(r'acessorioSession', AcessorioViewSet, basename='acessorio')

# ROTAS DE PERSONAGEM

router.register(r'personagem', PersonagemViewSet)

router.register(r'perfil', PerfilViewSet)
router.register(r'vidaPersonagem', VidaViewSet)
router.register(r'sanidadePersonagem', SanidadeViewSet)
router.register(r'ocultismoPersonagem', OcultismoViewSet)
router.register(r'esforcoPersonagem', EsforcoViewSet)
router.register(r'antescendentesPersonagem', AntescendentesPersonagemViewSet)
router.register(r'atributosPersonagem', AtributosPersonagemViewSet)
router.register(r'periciasPersonagem', PericiasPersonagemViewSet)
router.register(r'resistenciasPersonagem', ResistenciasPersonagemViewSet)
router.register(r'armamentosPersonagem', ArmamentosPersonagemViewSet)
router.register(r'acessoriosPersonagem', AcessoriosPersonagemViewSet)
router.register(r'inventarioPersonagem', IventarioViewSet)


urlpatterns = [
    path('token', GetToken.as_view()),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('registrar/', RegistrarView.as_view()),
    path('logout/', LogoutView.as_view(), name='logout'),
    
]
