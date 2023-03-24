from api.serializers.personagem import PersonagemSerializer
from personagem.models import Personagem
from rest_framework import viewsets, views
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from api.serializers.user import UserSerializer
from rest_framework.decorators import authentication_classes, permission_classes

class TokenAuthenticationCustom(TokenAuthentication):
    keyword = 'Token'
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #permission_classes = [IsAuthenticated]
from rest_framework import generics

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class LoginViewSet(views.APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)

@authentication_classes([TokenAuthenticationCustom])
@permission_classes([IsAuthenticated])
class PersonagemViewSet(viewsets.ModelViewSet):
    queryset = Personagem.objects.all()
    serializer_class = PersonagemSerializer
    def list(self, request, *args, **kwargs):
            itens_list = list()
            all_Personagem = Personagem.objects.all()
            for item in all_Personagem:
                item_full = dict()
                item_vida = dict()
                item_sanidade = dict()
                item_ocultismo = dict()
                item_esforco = dict()
                item_atributos = dict()
                atributo_dict = dict()
                item_full['id'] = item.id
                item_full['nome'] = item.nome
                item_full['origem'] = item.origem
                item_full['idade'] = item.idade
                item_full['naturalidade'] = item.naturalidade
                item_full['residencia'] = item.residencia
                item_full['classe'] = item.classe
                item_full['NEX'] = item.NEX   
                item_full['atributos'] = {'atributo': []}
                item_vida['atual'] = item.fk_vida.atual
                item_vida['maximo'] = item.fk_vida.maximo
                item_full['vida'] = item_vida
                
                item_sanidade['atual'] = item.fk_sanidade.atual 
                item_sanidade['maximo'] = item.fk_sanidade.maximo
                item_full['sanidade'] = item_sanidade
                
                item_ocultismo['atual'] = item.fk_ocultismo.atual
                item_ocultismo['maximo'] = item.fk_ocultismo.maximo
                item_full['ocultismo'] = item_ocultismo
                
                item_esforco['atual'] = item.fk_esforco.atual
                item_esforco['maximo'] = item.fk_esforco.maximo
                item_full['esforco'] = item_esforco
                
                for atributo in item.fk_atributos.fk_Atributo.all():
                    atributo_dict = {
                        'id': atributo.id,
                        'nome': atributo.nome,
                        'valor': atributo.valor
                    }
                    item_full['atributos']['atributo'].append(atributo_dict)
                    

                itens_list.append(item_full)

            res = { "personagem": itens_list }

            return Response(res, status=status.HTTP_200_OK)