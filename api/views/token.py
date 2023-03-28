from rest_framework.authtoken.views import ObtainAuthToken  
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics, permissions
for user in User.objects.all():
    Token.objects.get_or_create(user=user)
    
class GetToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request':request})
        
        serializer.is_valid(raise_exception=True)
        user = serializer._validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        
        return Response({'token': token.key,
                         'user_id':user.pk,
                         'username':user.username,
                         'email':user.email})
    
class LogoutView(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request, format=None):
        # Recupera o token do usuário atual
        token = Token.objects.get(user=request.user)
        # Apaga o token do banco de dados
        token.delete()
        # Retorna uma resposta vazia com o status HTTP 204 (No Content)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    