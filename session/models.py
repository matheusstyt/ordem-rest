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
        return f"{self.fk_mestre.username} | {self.id}"

class SolicitacaoJogador(models.Model):
    fk_sessao = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='solicitacao_jogador_fk_sessao_set')
    fk_mestre = models.ForeignKey(User, on_delete=models.CASCADE, related_name='solicitacao_jogador_fk_mestre_set')
    destino = models.ForeignKey(User, on_delete=models.CASCADE, related_name='solicitacao_jogador_destino_set')
    status = models.BooleanField(default=False) 
    def __str__(self) -> str:
        return self.fk_sessao.email
    
class JogadoresSessao(models.Model):
    fk_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='jogadoressessao_fk_user_set')
    fk_session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='jogadoressessao_fksession_set')
    data_inicio = models.CharField(max_length=100)
    status_online = models.BooleanField(default=False)
    def __str__(self) -> str:
        return f"{self.fk_user.username} / {self.fk_session.fk_mestre.username}"
    
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

class Acessorios(models.Model):
    descricao = models.CharField(max_length=100)
    obs = models.CharField(max_length=400)
    espaco = models.IntegerField()
    fk_user = models.ForeignKey(User, on_delete=models.CASCADE)

class Rituais(models.Model):
    descricao = models.CharField(max_length=100, blank=True)
    obs = models.CharField(max_length=400, blank=True)
    alcance = models.CharField(max_length=50, blank=True)
    dano_passivo = models.CharField(max_length=120, blank=True)
    dano_ativo = models.IntegerField( blank=True)
    tipo = models.CharField(max_length=30, blank=True)
    ocultismo = models.IntegerField( blank=True)
    categoria = models.CharField(max_length=50, blank=True)
    fk_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)


class Armamento(models.Model):
    descricao = models.CharField(max_length=120)
    categoria_1 = models.CharField(max_length=50)
    categoria_2 = models.CharField(max_length=50)
    categoria_3 = models.CharField(max_length=70)
    alcance = models.CharField(max_length=50)
    dano_passivo = models.CharField(max_length=120)
    dano_ativo = models.IntegerField()
    tipo = models.CharField(max_length=30)
    espaco = models.IntegerField()
    fk_user = models.ForeignKey(User, on_delete=models.CASCADE)
    
class ArmamentoUser(models.Model):
    fk_user = models.ForeignKey(User, on_delete=models.CASCADE)
    fk_armamento = models.ForeignKey(Armamento, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
class Atributo(models.Model):
    nome = models.CharField(max_length=50)
    valor = models.IntegerField()
    
class Atributos(models.Model):
    fk_atributo = models.ForeignKey(Atributo, on_delete= models.CASCADE)
    fk_session = models.ForeignKey(Session, on_delete=models.CASCADE)

class Pericia(models.Model):
    nome = models.CharField(max_length=50)
    valor = models.IntegerField()
    
class Pericias(models.Model):
    fk_pericia = models.ForeignKey(Pericia, on_delete= models.CASCADE)
    fk_session = models.ForeignKey(Session, on_delete=models.CASCADE)
    
class Resistencia(models.Model):
    nome = models.CharField(max_length=50)
    valor = models.IntegerField()
    
class Resistencias(models.Model):
    fk_resistencia = models.ForeignKey(Resistencia, on_delete= models.CASCADE)
    fk_session = models.ForeignKey(Session, on_delete=models.CASCADE)