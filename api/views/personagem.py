from rest_framework.viewsets import ModelViewSet
from rest_framework import views, filters
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes
from django_filters.rest_framework import DjangoFilterBackend

from api.serializers.personagem import *
from personagem.models import *

#@permission_classes([IsAuthenticated])
class PersonagemViewSet(ModelViewSet):
    queryset = Personagem.objects.all()
    serializer_class = PersonagemSerializer
    def list(self, request, *args, **kwargs):
            itens_list = list()
            all_Personagem = Personagem.objects.all()
            for item in all_Personagem:
                item_full = dict()

                item_full['id'] = item.id
                item_full['nome'] = item.nome
                item_full['origem'] = item.origem
                item_full['idade'] = item.idade
                item_full['naturalidade'] = item.naturalidade
                item_full['residencia'] = item.residencia
                item_full['classe'] = item.classe
                item_full['NEX'] = item.NEX   
                
                item_full['lesao_grave'] = item.lesao_grave
                item_full['inconsciente'] = item.inconsciente
                item_full['morrendo'] = item.morrendo
                item_full['traumatizado'] = item.traumatizado
                item_full['enlouquecendo'] = item.enlouquecendo

                #DICIONÁRIOS DAS BARRAS
                item_vida = dict()
                item_sanidade = dict()
                item_ocultismo = dict()
                item_esforco = dict()

                item_full['vida'] = {}
                item_full['sanidade']  = {} 
                item_full['ocultismo'] = {}
                item_full['esforco'] = {}

                item_vida = { "atual" : item.fk_vida.atual, "maximo" : item.fk_vida.maximo }
                item_sanidade = { "atual" : item.fk_sanidade.atual, "maximo" : item.fk_sanidade.maximo }
                item_ocultismo = { "atual" : item.fk_ocultismo.atual, "maximo" : item.fk_ocultismo.maximo }
                item_esforco = { "atual" : item.fk_esforco.atual, "maximo" : item.fk_esforco.maximo }

                item_full['vida'].append(item_vida)
                item_full['sanidade'].append(item_sanidade)
                item_full['ocultismo'].append(item_ocultismo)
                item_full['esforco'].append(item_esforco)

                # CADEIAS EM JSON 
                item_full['antescendentes'] = item.fk_antescendentes.cadeia
                item_full['atributos'] = item.fk_atributos.cadeia
                item_full['pericias'] = item.fk_pericias.cadeia
                item_full['resistencias'] = item.fk_resistencias
                
                # LOOP EM VÁRIOS OBJETOS 
                # ARMAMENTOS
                armamentos = ArmamentosPersonagem.objects.get(fk_personagem = item.id)
                armamento_dict = dict()

                item_full['armamentos'] = {'armamento': []}

                for arma in armamentos:
                    armamento_dict = {
                         
                        'id': arma.id,
                        'nome': arma.nome,
                        'categoria_0': arma.categoria_0,
                        'categoria_1': arma.categoria_1,
                        'categoria_2': arma.categoria_2,
                        'alcance': arma.alcance,
                        'critico': arma.critico,
                        'dano': arma.dano,
                        'espaco': arma.espaco,
                        'tipo': arma.tipo,
                        'fk_personagem': arma.fk_personagem,
                    }
                    
                    item_full['armamentos']['armamento'].append(armamento_dict)

                #ACESSÓRIOS
                acessorios = AcessoriosPersonagem.objects.get(fk_personagem = item.id)
                acessorio_dict = dict()

                item_full['acessorios'] = {'acessorio': []}

                for acessorio in acessorios:
                    acessorio_dict = {
                         
                        'id': acessorio.id,
                        'nome': acessorio.nome,
                        'descricao': acessorio.descricao,
                        'espaco': acessorio.espaco,
                        'fk_personagem': acessorio.fk_personagem,
                    }
                    
                    item_full['acessorios']['acessorio'].append(acessorio_dict)
                itens_list.append(item_full)

            res = { "personagem": itens_list }

            return Response(res, status=status.HTTP_200_OK)
    
#@permission_classes([IsAuthenticated])
class VidaViewSet(ModelViewSet):
     queryset = VidaBar.objects.all()
     serializer_class = VidaBarSerializer
     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
     filterset_fields = ['id']
     search_fields = ['id']

#@permission_classes([IsAuthenticated])
class SanidadeViewSet(ModelViewSet):
     queryset = SanidadeBar.objects.all()
     serializer_class = SanidadeBarSerializer
     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
     filterset_fields = ['id']
     search_fields = ['id']

#@permission_classes([IsAuthenticated])
class OcultismoViewSet(ModelViewSet):
     queryset = OcultismoBar.objects.all()
     serializer_class = OcultismoBarSerializer
     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
     filterset_fields = ['id']
     search_fields = ['id']

#@permission_classes([IsAuthenticated])
class EsforcoViewSet(ModelViewSet):
     queryset = EsforcoBar.objects.all()
     serializer_class = EsforcoBarSerializer
     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
     filterset_fields = ['id']
     search_fields = ['id']

#@permission_classes([IsAuthenticated])
class AntescendentesPersonagemViewSet(ModelViewSet):
     queryset = AntescendentesPersonagem.objects.all()
     serializer_class = AntescendentesPersonagemSerializer
     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
     filterset_fields = ['id']
     search_fields = ['id']

#@permission_classes([IsAuthenticated])
class AtributosPersonagemViewSet(ModelViewSet):
     queryset = AtributosPersonagem.objects.all()
     serializer_class = AtributosPersonagemSerializer
     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
     filterset_fields = ['id']
     search_fields = ['id']

#@permission_classes([IsAuthenticated])
class PericiasPersonagemViewSet(ModelViewSet):
     queryset = PericiasPersonagem.objects.all()
     serializer_class = PericiasPersonagemSerializer
     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
     filterset_fields = ['id']
     search_fields = ['id']

#@permission_classes([IsAuthenticated])
class ResistenciasPersonagemViewSet(ModelViewSet):
     queryset = ResistenciasPersonagem.objects.all()
     serializer_class = ResistenciasPersonagemSerializer
     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
     filterset_fields = ['id']
     search_fields = ['id']

#@permission_classes([IsAuthenticated])
class ArmamentosPersonagemViewSet(ModelViewSet):
     queryset = ArmamentosPersonagem.objects.all()
     serializer_class = ArmamentosPersonagemSerializer
     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
     filterset_fields = ['fk_personagem']
     search_fields = ['fk_personagem']

#@permission_classes([IsAuthenticated])
class AcessoriosPersonagemViewSet(ModelViewSet):
     queryset = AcessoriosPersonagem.objects.all()
     serializer_class = AcessoriosPersonagemSerializer
     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
     filterset_fields = ['fk_personagem']
     search_fields = ['fk_personagem']

#@permission_classes([IsAuthenticated])
class IventarioViewSet(ModelViewSet):
     queryset = Iventario.objects.all()
     serializer_class = IventarioSerializer
     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
     filterset_fields = ['fk_personagem']
     search_fields = ['fk_personagem']
