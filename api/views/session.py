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
    queryset = Session.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    def retrieve(self, request, *args, **kwargs):
        session_id = kwargs.get('pk')
        session = Session.objects.filter(pk=session_id).first()
        if not session:
            return Response(status=status.HTTP_404_NOT_FOUND)

        players = JogadoresSessao.objects.filter(fk_session=session_id)
        players_list = []
        for player in players:
            players_list.append({
                'id': player.id,
                'fk_user': player.fk_user.id,
                'fk_session': player.fk_session.id,
                'data_inicio': player.data_inicio,
                'player': player.fk_user.username,
                'mestre': player.fk_session.fk_mestre.username,
                'status': player.status_online,
            })

        response_data = {
            'id': session.id,
            'fk_mestre': session.fk_mestre.id,
            'mestre': session.fk_mestre.username,
            'descricao': session.descricao,
            'data_criacao': session.data_criacao,
            'status': session.status,
            'players': players_list,
        }

        return Response({'session': response_data})
    
    def list(self, request, *args, **kwargs):
        sessions = Session.objects.filter(fk_mestre=request.user)
        items = []
        for session in sessions:
            players = JogadoresSessao.objects.filter(fk_session=session.id)
            players_list = []
            for player in players:
                players_list.append({
                    'id': player.id,
                    'fk_user': player.fk_user.id,
                    'fk_session': player.fk_session.id,
                    'data_inicio': player.data_inicio,
                    'player': player.fk_user.username,
                    'mestre': player.fk_session.fk_mestre.username,
                    'status': player.status_online,
                })
            items.append({
                'id': session.id,
                'fk_mestre': session.fk_mestre.id,
                'mestre': session.fk_mestre.username,
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

class JogadoresSessaoViewSet(viewsets.ModelViewSet):
    queryset = JogadoresSessao.objects.all()
    serializer_class = JogadoresSessaoSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    # def retrieve(self, request, *args, **kwargs):
    #     player_id = kwargs.get('pk')
    #     player = JogadoresSessao.objects.filter(fk_user=player_id).first()
    #     if not player:
    #         return Response(status=status.HTTP_404_NOT_FOUND)

    #     body = {
    #         'id': player.id,
    #         'fk_user': player.fk_user.id,
    #         'fk_session': player.fk_session.id,
    #         'data_inicio': player.data_inicio,
    #         'player': player.fk_user.username,
    #         'mestre': player.fk_session.fk_mestre.username,
    #         'status': player.status_online,
    #     }
 
    #     return Response({'player': body})
    
    def list(self, request, *args, **kwargs):
        print(request.data)
        fk_user = request.query_params.get('fk_user', None)
        if fk_user is None:
            # Retorna todos os jogadores de sessões de qualquer usuário
            list_players = JogadoresSessao.objects.all()
        else:
            # Filtra os jogadores de sessões do usuário logado pelo parâmetro fk_session
            list_players = JogadoresSessao.objects.filter(fk_user=fk_user)

        items = []
        for player in list_players:
            items.append({      
                'id': player.id,
                'fk_user': player.fk_user.id,
                'fk_session': player.fk_session.id,
                'data_inicio': player.data_inicio,
                'player': player.fk_user.username,
                'mestre': player.fk_session.fk_mestre.username,
                'fk_mestre': player.fk_session.fk_mestre.id,
                'status': player.status_online,
            })
        return Response({'players': items})


class SolicitacaoJogadorViewSet(viewsets.ModelViewSet):
    queryset = SolicitacaoJogador.objects.all()
    serializer_class = SolicitacaoJogadorSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def list(self, request, *args, **kwargs):
        solicitacoes = SolicitacaoJogador.objects.filter(destino=request.user)
        items = []
        for solicitacao in solicitacoes:

            items.append({
                'id': solicitacao.id,
                'fk_sessao': solicitacao.fk_sessao.id,
                'fk_mestre': solicitacao.fk_mestre.id,
                'fk_destino': solicitacao.destino.id,
                'destino': solicitacao.destino.username,
                'mestre': solicitacao.fk_mestre.username,
                'status': solicitacao.status,
 
            })
        return Response({'askplayer': items})

class AtributosViewSet(viewsets.ModelViewSet):
    queryset = Atributos.objects.all()
    serializer_class = AtributosSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['fk_session']
    search_fields = ['fk_session']
    ordering_fields = ['fk_session']
    def create(self, request, *args, **kwargs):
        fk_atributo = request.data['fk_atributo']
        if Atributos.objects.filter(fk_atributo = fk_atributo).exists():
            atributos_existente = Atributos.objects.get(fk_atributo = fk_atributo)
            serializer = self.get_serializer(atributos_existente)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            print('NAO TEM')
            return super().create(request, *args, **kwargs)

class AtributoViewSet(viewsets.ModelViewSet):
    queryset = Atributo.objects.all()
    serializer_class = AtributoSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['id']
    search_fields = ['id']
    ordering_fields = ['id']
    
    def create(self, request, *args, **kwargs):
        nome = request.data['nome']
        if Atributo.objects.filter(nome = nome).exists():
            atributo_existente = Atributo.objects.get(nome = nome)
            serializer = self.get_serializer(atributo_existente)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return super().create(request, *args, **kwargs)

class PericiasViewSet(viewsets.ModelViewSet):
    queryset = Pericias.objects.all()
    serializer_class = PericiasSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['fk_session']
    search_fields = ['fk_session']
    ordering_fields = ['fk_session']
    def create(self, request, *args, **kwargs):
        fk_pericia = request.data['fk_pericia']
        if Pericias.objects.filter(fk_pericia = fk_pericia).exists():
            pericias_existente = Pericias.objects.get(fk_pericia = fk_pericia)
            serializer = self.get_serializer(pericias_existente)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            print('NAO TEM')
            return super().create(request, *args, **kwargs)

class PericiaViewSet(viewsets.ModelViewSet):
    queryset = Pericia.objects.all()
    serializer_class = PericiaSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['id']
    search_fields = ['id']
    ordering_fields = ['id']
    
    def create(self, request, *args, **kwargs):
        nome = request.data['nome']
        if Pericia.objects.filter(nome = nome).exists():
            pericia_existente = Pericia.objects.get(nome = nome)
            serializer = self.get_serializer(pericia_existente)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return super().create(request, *args, **kwargs)

class ResistenciasViewSet(viewsets.ModelViewSet):
    queryset = Resistencias.objects.all()
    serializer_class = ResistenciasSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['fk_session']
    search_fields = ['fk_session']
    ordering_fields = ['fk_session']
    
    def create(self, request, *args, **kwargs):
        fk_resistencia = request.data['fk_resistencia']
        if Resistencias.objects.filter(fk_resistencia = fk_resistencia).exists():
            resistencias_existente = Resistencias.objects.get(fk_resistencia = fk_resistencia)
            serializer = self.get_serializer(resistencias_existente)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            print('NAO TEM')
            return super().create(request, *args, **kwargs)
class ResistenciaViewSet(viewsets.ModelViewSet):
    queryset = Resistencia.objects.all()
    serializer_class = ResistenciaSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['id']
    search_fields = ['id']
    ordering_fields = ['id']
    
    def create(self, request, *args, **kwargs):
        nome = request.data['nome']
        if Resistencia.objects.filter(nome = nome).exists():
            resistencias_existente = Resistencia.objects.get(nome = nome)
            serializer = self.get_serializer(resistencias_existente)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            print('NAO TEM')
            return super().create(request, *args, **kwargs)