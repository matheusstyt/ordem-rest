from rest_framework import serializers
from django.contrib.auth.models import User

from session.models import FriendList, SolicitacaoContato

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class FriendListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendList
        fields = "__all__"
class SolicitacaoContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolicitacaoContato
        fields = "__all__"
