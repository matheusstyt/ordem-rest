from django.db import models
from django.contrib.auth.models import User

class FriendList(models.Model):
    fk_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friendlist_user_set')
    fk_friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friendlist_friend_set')
    data_inicio = models.CharField(max_length=100)
    status_online = models.BooleanField(default=False)
    def __str__(self) -> str:
        return f"{self.fk_user.username} / {self.fk_friend.username}"
    
class SolicitacaoContato(models.Model):
    origem = models.ForeignKey(User, on_delete=models.CASCADE, related_name='solicitacao_contato_origem_set')
    destino = models.ForeignKey(User, on_delete=models.CASCADE, related_name='solicitacao_contato_destino_set')
    status = models.BooleanField(default=False) 
# Create your models here.
class Session(models.Model):
    fk_mestre = models.ForeignKey(User, on_delete=models.CASCADE)
    data_criacao = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.fk_mestre.email
    
class SessionLog(models.Model):
    fk_session = models.ForeignKey(Session, on_delete=models.CASCADE)
    data_modificacao = models.DateTimeField()
    descricao = models.CharField(max_length=200, blank=True)
    origem = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.descricao
    
class SessionPlayers(models.Model):
    fk_session = models.ForeignKey(Session, on_delete=models.CASCADE)
    fk_player = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.fk_player.email
    
class Solicitacao(models.Model):
    fk_session = models.ForeignKey(Session, on_delete=models.CASCADE)
    fk_de = models.ForeignKey(User, on_delete=models.CASCADE, related_name='solicitacao_de_set')
    fk_para = models.ForeignKey(User, on_delete=models.CASCADE, related_name='solicitacao_para_set')
    status = models.BooleanField(default=False) 
    