
from personagem.models import Personagem
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
        