from rest_framework import viewsets
from api.serializers.session import *
from session.models import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions

from rest_framework import status
class SessionViewSet(viewsets.ModelViewSet):
    serializer_class = SessionSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Session.objects.all()
    
    def list(self, request, *args, **kwargs):
        itens_list = list()
        all_Session = Session.objects.all()
        all_Player = SessionPlayers.objects.all()
        for session in all_Session:
            item_full = dict()  
            player_list = list()
            item_full['id'] = session.id
            item_full['fk_mestre'] = session.fk_mestre.id
            item_full['data_criacao'] = session.data_criacao
            item_full['qtd_max'] = session.qtd_max
            item_full['status'] = session.status
            for player in all_Player:
                if player.fk_session.id == session.id:
                    player_dict = {
                        'id': player.fk_player.id,
                        'status': player.status,
                    }
                    player_list.append(player_dict)
                    
            item_full['players'] = player_list
            itens_list.append(item_full)    
            
        res = { "session": itens_list }
        return Response(res, status=status.HTTP_200_OK)