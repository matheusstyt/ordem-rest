from rest_framework import routers
from django.contrib import admin
from django.urls import include, path
from api.views.token import GetToken
from api.views.user import PersonagemViewSet, UserViewSet
from rest_framework.authtoken import views
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'personagem', PersonagemViewSet)

urlpatterns = [
    path('token', GetToken.as_view()),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    
]
