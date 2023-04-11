
from personagem.models import *
from rest_framework import serializers
from django.contrib.auth.models import User
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class PersonagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personagem
        fields = "__all__"
from personagem.models import Personagem
from rest_framework import serializers
from django.contrib.auth.models import User
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class VidaBarSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = VidaBar
        fields = "__all__"
class SanidadeBarSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SanidadeBar
        fields = "__all__"
class OcultismoBarSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OcultismoBar
        fields = "__all__"
class EsforcoBarSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = EsforcoBar
        fields = "__all__"
class AntescendentesPersonagemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AntescendentesPersonagem
        fields = "__all__"
class AtributosPersonagemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AtributosPersonagem
        fields = "__all__"
class PericiasPersonagemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PericiasPersonagem
        fields = "__all__"
        
class ResistenciasPersonagemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ResistenciasPersonagem
        fields = "__all__"
class ArmamentosPersonagemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ArmamentosPersonagem
        fields = "__all__"
class AcessoriosPersonagemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AcessoriosPersonagem
        fields = "__all__"

class IventarioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Iventario
        fields = "__all__"