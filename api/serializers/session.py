
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