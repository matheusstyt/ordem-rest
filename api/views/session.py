from api.serializers.session import *
from session.models import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from session.filters import SessionFilter
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, permissions, viewsets
class SessionViewSet(viewsets.ModelViewSet):
    serializer_class = SessionSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['descricao']
    search_fields = ['fk_mestre__username']
    ordering_fields = ['data_criacao']

    def list(self, request, *args, **kwargs):
        sessions = Session.objects.filter(fk_mestre=request.user)
        items = []
        for session in sessions:
            players = SessionPlayers.objects.filter(fk_session=session)
            players_list = []
            for player in players:
                players_list.append({
                    'id': player.fk_player.id,
                    'status': player.status,
                })
            items.append({
                'id': session.id,
                'fk_mestre': session.fk_mestre.id,
                'descricao': session.descricao,
                'data_criacao': session.data_criacao,
                'status': session.status,
                'players': players_list,
            })
        return Response({'session': items})
class ArmamentosUserViewSet(viewsets.ModelViewSet):
    serializer_class = ArmamentoSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['id']
    search_fields = ['id']
    ordering_fields = ['id']
class ArmamentosViewSet(viewsets.ModelViewSet):
    queryset = Armamento.objects.all()
    serializer_class = ArmamentoSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['fk_user']
    search_fields = ['fk_user']
    ordering_fields = ['fk_user']

class AcessoriosViewSet(viewsets.ModelViewSet):
    queryset = Acessorios.objects.all()
    serializer_class = AcessoriosSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['fk_user']
    search_fields = ['fk_user']
    ordering_fields = ['fk_user']

class RituaisViewSet(viewsets.ModelViewSet):
    queryset = Rituais.objects.all()
    serializer_class = RituaisSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['fk_user']
    search_fields = ['fk_user']
    ordering_fields = ['fk_user']
