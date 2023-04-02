from rest_framework import routers
from django.contrib import admin
from django.urls import include, path

from api.views.token import GetToken, LogoutView
from api.views.session import *
from api.views.user import *
from rest_framework.authtoken import views
router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
#router.register(r'registrar', RegistrarView.as_view(), basename='user')
router.register(r'contact', FriendListViewSet, basename='FriendList')
router.register(r'ask', SolicitacaoContatoViewSet, basename='solicitacaocontato')
router.register(r'personagem', PersonagemViewSet)
router.register(r'session', SessionViewSet, basename='session')
router.register(r'armamento', ArmamentosViewSet, basename='armamento')
router.register(r'acessorios', AcessoriosViewSet, basename='acessorios')
router.register(r'rituais', RituaisViewSet, basename='rituais')
router.register(r'armamentoUser', SessionViewSet, basename='session')

router.register(r'askplayer', SolicitacaoJogadorViewSet, basename='JogadoresSessao')
router.register(r'players', JogadoresSessaoViewSet, basename='SolicitacaoJogador')
router.register(r'atributo', AtributoViewSet, basename='atributo')
router.register(r'atributos', AtributosViewSet, basename='atributos')
router.register(r'pericia', PericiaViewSet, basename='pericia')
router.register(r'pericias', PericiasViewSet, basename='pericias')
urlpatterns = [
    path('token', GetToken.as_view()),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('registrar/', RegistrarView.as_view()),
    path('logout/', LogoutView.as_view(), name='logout'),
    
]
