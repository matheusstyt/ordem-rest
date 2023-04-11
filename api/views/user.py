from api.serializers.personagem import PersonagemSerializer
from personagem.models import Personagem
from rest_framework import viewsets, views, filters
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from api.serializers.user import FriendListSerializer, SolicitacaoContatoSerializer, UserSerializer
from rest_framework.decorators import authentication_classes, permission_classes
from django_filters.rest_framework import DjangoFilterBackend

from session.models import FriendList, SolicitacaoContato

class TokenAuthenticationCustom(TokenAuthentication):
    keyword = 'Token'
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['username']
    search_fields = ['username']

from rest_framework import generics

class UserList(views.APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        queryset = User.objects.all()  # obtenha todos os usuários
        username_query = request.GET.get('username')  # obtenha o parâmetro de consulta 'username'

        if username_query:  # se o parâmetro de consulta 'username' estiver presente
            queryset = queryset.filter(username__icontains=username_query)  # filtre os usuários com base no nome de usuário

        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

class FriendListViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = FriendList.objects.all()
    serializer_class = FriendListSerializer

    def list(self, request, *args, **kwargs):
        contacts = FriendList.objects.filter(fk_user=request.user)
        items = []
        for contact in contacts:

            items.append({
                'id': contact.id,
                'fk_user': contact.fk_user.username,
                'fk_friend': contact.fk_friend.username,
                'data_inicio': contact.data_inicio,
                'status_online': contact.status_online,
 
            })
        return Response({'list_contact': items})

class SolicitacaoContatoViewSet(viewsets.ModelViewSet):
    queryset = SolicitacaoContato.objects.all()
    serializer_class = SolicitacaoContatoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        solicitacoes = SolicitacaoContato.objects.filter(destino=request.user)
        items = []
        for solicitacao in solicitacoes:

            items.append({
                'id': solicitacao.id,
                'origem': solicitacao.origem.username,
                'destino': solicitacao.destino.username,
                'fk_origem': solicitacao.origem.id,
                'fk_destino': solicitacao.destino.id,
                'status': solicitacao.status,
 
            })
        return Response({'ask': items})
    
class LoginViewSet(views.APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)

class RegistrarView(views.APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request, format=None):
        return Response(status=status.HTTP_200_OK)
    def post(self, request, format=None):
        user_email = request.data["email"]
        user_username = request.data['username']
        user_password = request.data['password']
        
        if(User.objects.filter(email=user_email, username=user_username).exists()):
            return Response(status=status.HTTP_403_FORBIDDEN)
        else:
            try:
                user = User.objects.create_user(username=user_username, email=user_email, password=user_password)

                user_serializer = UserSerializer(user)

                res = { 'user_data' : user_serializer.data}

                return Response(res, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response(e, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    