from django.db import models
from django.contrib.auth.models import User

from session.models import Session 
from django_base64field.fields import Base64Field

class VidaBar(models.Model):
    atual = models.IntegerField()
    maximo = models.IntegerField()
    def __str__(self) -> str:
            return f'{str(self.atual)} de {str(self.maximo)}'
        
class SanidadeBar(models.Model):
    atual = models.IntegerField()
    maximo = models.IntegerField()
    def __str__(self) -> str:
        
            return f'{str(self.atual)} de {str(self.maximo)}'
class OcultismoBar(models.Model):
    atual = models.IntegerField()
    maximo = models.IntegerField()
    def __str__(self) -> str:
            return f'{str(self.atual)} de {str(self.maximo)}'
        
class EsforcoBar(models.Model):
    atual = models.IntegerField()
    maximo = models.IntegerField()
    temporario = models.IntegerField(default=0)
    def __str__(self) -> str:
            return f'{str(self.atual)} de {str(self.maximo)}'
  
# class Antescendente(models.Model):
#     nome = models.CharField(max_length=100, blank=True, null=True)
#     descricao = models.CharField(max_length=100, blank=True, null=True)
#     def __str__(self) -> str:
#         return self.nome   
class AntescendentesPersonagem(models.Model):
 #   fk_Antescendente = models.ForeignKey(Antescendente, blank=True, null=True)
    cadeia = models.CharField(max_length=5000)
    def __str__(self) -> str:
            return 'Cadeia de antescendentes'
# class Atributo(models.Model):
#     nome = models.CharField(max_length=100, blank=True, null=True)
#     valor = models.IntegerField()
#     def __str__(self) -> str:
#         return self.nome 
    
class AtributosPersonagem(models.Model):
#    fk_Atributo = models.ForeignKey(Atributo, blank=True, null=True)
    cadeia = models.CharField(max_length=5000)
    def __str__(self) -> str:
            return 'Cadeia de atributos'
    
# class Pericia(models.Model):
#     nome = models.CharField(max_length=100, blank=True, null=True)
#     valor = models.IntegerField()
#     def __str__(self) -> str:
#         return self.nome 
    
class PericiasPersonagem(models.Model):
#    fk_Pericia = models.ForeignKey(Pericia, blank=True, null=True)
    cadeia = models.CharField(max_length=5000)
    def __str__(self) -> str:
            return 'Cadeia de pericias'
    
# class Resistencia(models.Model):
#     nome = models.CharField(max_length=100, blank=True, null=True)
#     valor = models.IntegerField()
#     def __str__(self) -> str:
#         return self.nome 
    
class ResistenciasPersonagem(models.Model):
#    fk_Resistencia = models.ForeignKey(Resistencia, blank=True, null=True)
    cadeia = models.CharField(max_length=5000)
    def __str__(self) -> str:
        return 'Cadeia de resistencias'

class PerfilImage(models.Model):
    image = Base64Field(max_length=900000, blank=True, null=True)
    
class Personagem(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    origem = models.CharField(max_length=100, blank=True, null=True)
    idade = models.IntegerField(blank=True, null=True)
    classe = models.CharField(max_length=100, blank=True, null=True)
    NEX = models.IntegerField(default= 0)
    trilha = models.CharField(max_length=100, blank=True, null=True)
    patente = models.CharField(max_length=100, blank=True, null=True)
    naturalidade = models.CharField(max_length=100, blank=True, null=True)
    residencia = models.CharField(max_length=100, blank=True, null=True)
    
    
    lesao_grave = models.BooleanField(default=False)
    inconsciente = models.BooleanField(default=False)
    morrendo = models.BooleanField(default=False)
    traumatizado = models.BooleanField(default=False)
    enlouquecendo = models.BooleanField(default=False)

    fk_vida = models.OneToOneField(VidaBar, on_delete=models.CASCADE)
    fk_sanidade = models.OneToOneField(SanidadeBar, on_delete=models.CASCADE, blank=True)
    fk_ocultismo = models.OneToOneField(OcultismoBar, on_delete=models.CASCADE, blank=True)
    fk_esforco = models.OneToOneField(EsforcoBar, on_delete=models.CASCADE)
    
    fk_atributos = models.OneToOneField(AtributosPersonagem, on_delete=models.CASCADE)
    fk_pericias = models.OneToOneField(PericiasPersonagem, on_delete=models.CASCADE, blank=True)
    fk_resistencias = models.OneToOneField(ResistenciasPersonagem, on_delete=models.CASCADE, blank=True)
    fk_antescendentes = models.OneToOneField(AntescendentesPersonagem, on_delete=models.CASCADE, blank=True)
    
    fk_perfil_img = models.OneToOneField(PerfilImage, on_delete=models.CASCADE)
    fk_session = models.ForeignKey(Session, on_delete=models.CASCADE)
    fk_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nome
    
class ArmamentosPersonagem(models.Model):
    arma = models.CharField(max_length=100, blank=True, null=True)
    categoria_0 = models.CharField(max_length=100, blank=True, null=True)
    categoria_1 = models.CharField(max_length=100, blank=True, null=True)
    categoria_2 = models.CharField(max_length=100, blank=True, null=True)
    alcance = models.CharField(max_length=100, blank=True, null=True)
    critico = models.CharField(max_length=100, blank=True, null=True)
    dano = models.CharField(max_length=100, blank=True, null=True)
    espaco = models.IntegerField()
    tipo = models.CharField(max_length=100, blank=True, null=True)
    
    fk_personagem = models.ForeignKey(Personagem, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.arma

class AcessoriosPersonagem(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    descricao = models.CharField(max_length=400, blank=True, null=True)
    espaco = models.IntegerField(blank=True, null=True)

    fk_personagem = models.ForeignKey(Personagem, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.descricao

class Iventario(models.Model):
    espaco_total = models.IntegerField()

    fk_armamentos = models.ForeignKey(ArmamentosPersonagem, on_delete= models.CASCADE, blank=True, null=True)
    fk_acessorios = models.ForeignKey(AcessoriosPersonagem, on_delete= models.CASCADE, blank=True, null=True)
    fk_personagem = models.CharField(max_length=50)
    def __str__(self) -> str:
        return str(self.espaco_total)

class Perfil(models.Model):
    image = Base64Field(max_length=900000, blank=True, null=True)
    fk_personagem = models.ForeignKey(Personagem, on_delete= models.CASCADE, blank=True, null=True)
