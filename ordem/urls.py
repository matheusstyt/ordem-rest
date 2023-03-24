from rest_framework import routers
from django.contrib import admin
from django.urls import include, path
from api.views.token import GetToken
from api.views.session import SessionViewSet
from api.views.user import PersonagemViewSet, UserList, UserViewSet
from rest_framework.authtoken import views
router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'personagem', PersonagemViewSet)
router.register(r'session', SessionViewSet)
urlpatterns = [
    path('token', GetToken.as_view()),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    
]
