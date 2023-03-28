from rest_framework import routers
from django.contrib import admin
from django.urls import include, path

from api.views.token import GetToken, LogoutView
from api.views.session import SessionViewSet
from api.views.user import FriendListViewSet, PersonagemViewSet, RegistrarView, SolicitacaoContatoViewSet, UserList, UserViewSet
from rest_framework.authtoken import views
router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
#router.register(r'registrar', RegistrarView.as_view(), basename='user')
router.register(r'contact', FriendListViewSet, basename='FriendList')
router.register(r'ask', SolicitacaoContatoViewSet, basename='solicitacaocontato')
router.register(r'personagem', PersonagemViewSet)
router.register(r'session', SessionViewSet, basename='session')
router.register(r'armamento', SessionViewSet, basename='session')
router.register(r'armamentoUser', SessionViewSet, basename='session')
urlpatterns = [
    path('token', GetToken.as_view()),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('registrar/', RegistrarView.as_view()),
    path('logout/', LogoutView.as_view(), name='logout'),
    
]
