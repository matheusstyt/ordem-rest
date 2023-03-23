
from session.models import *
from rest_framework import serializers
class SessionSerializer(serializers.Serializer):
    class Meta:
        model = Session
        fields = "__all__"
