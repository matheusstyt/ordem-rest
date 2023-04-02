
from session.models import *
from rest_framework import serializers
class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = "__all__"
class ArmamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Armamento
        fields = "__all__"
class ArmamentoUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArmamentoUser
        fields = "__all__"
class AcessoriosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acessorios
        fields = "__all__"
class RituaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rituais
        fields = "__all__"

class SolicitacaoJogadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolicitacaoJogador
        fields = "__all__"
        
class JogadoresSessaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = JogadoresSessao
        fields = "__all__"
        
class AtributosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atributos
        fields = "__all__"
class AtributoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atributo
        fields = "__all__"
        
class PericiasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pericias
        fields = "__all__"
class PericiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pericia
        fields = "__all__"