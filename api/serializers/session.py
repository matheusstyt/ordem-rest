
from session.models import *
from session.models import Armamento as armamento, Armamentos as armamentos
from rest_framework import serializers
class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
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

class ResistenciasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resistencias
        fields = "__all__"
class ResistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resistencia
        fields = "__all__"

class ArmamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = armamento
        fields = "__all__"
class ArmamentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = armamentos
        fields = "__all__"

class AcessorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acessorio
        fields = "__all__"
class AcessoriosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acessorios
        fields = "__all__"