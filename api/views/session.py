from rest_framework import viewsets
from api.serializers.session import *
from session.models import *
from rest_framework.response import Response
from rest_framework import status
class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
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