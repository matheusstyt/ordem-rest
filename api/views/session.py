from rest_framework import viewsets
from api.serializers.session import *
from session.models import *

class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    