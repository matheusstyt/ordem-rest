from django.db import models
from django.contrib.auth.models import User 

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
    temporario = models.IntegerField()
    def __str__(self) -> str:
            return f'{str(self.atual)} de {str(self.maximo)}'
    
class Armamento(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    categoria_1 = models.IntegerField()
    categoria_2 = models.CharField(max_length=100, blank=True, null=True)
    dano = models.IntegerField()
    critico = models.CharField(max_length=100, blank=True, null=True)
    alcance = models.IntegerField()
    tipo = models.CharField(max_length=100, blank=True, null=True)
    peso = models.IntegerField()
    def __str__(self) -> str:
        return self.nome

class Item(models.Model):
    descricao = models.CharField(max_length=100, blank=True, null=True)
    peso = models.IntegerField(blank=True, null=True)
    def __str__(self) -> str:
        return self.descricao
  
class Antescendente(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    descricao = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self) -> str:
        return self.nome   
class Antescendentes(models.Model):
    fk_Antescendente = models.ManyToManyField(Antescendente, blank=True, null=True)
    
class Atributo(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    valor = models.IntegerField()
    def __str__(self) -> str:
        return self.nome 
class Atributos(models.Model):
    fk_Atributo = models.ManyToManyField(Atributo, blank=True, null=True)
    def __str__(self) -> str:
            return 'Cadeia de atributos'
class Pericia(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    valor = models.IntegerField()
    def __str__(self) -> str:
        return self.nome 
class Pericias(models.Model):
    
    fk_Pericia = models.ManyToManyField(Pericia, blank=True, null=True)
    def __str__(self) -> str:
            return 'Cadeia de pericias'
class Resistencia(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    valor = models.IntegerField()
    def __str__(self) -> str:
        return self.nome 
class Resistencias(models.Model):
    fk_Resistencia = models.ManyToManyField(Resistencia, blank=True, null=True)
    def __str__(self) -> str:
        return 'Cadeia de resistencias'
class Iventario(models.Model):
    fk_armamento = models.ManyToManyField(Armamento, blank=True, null=True)
    fk_item = models.ManyToManyField(Item, blank=True, null=True)
    espaco_total = models.IntegerField()
    def __str__(self) -> str:
        return str(self.espaco_total)
    
class Personagem(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    origem = models.CharField(max_length=100, blank=True, null=True)
    idade = models.IntegerField()
    naturalidade = models.CharField(max_length=100, blank=True, null=True)
    residencia = models.CharField(max_length=100, blank=True, null=True)
    classe = models.CharField(max_length=100, blank=True, null=True)
    NEX = models.IntegerField()
    
    fk_vida = models.OneToOneField(VidaBar, on_delete=models.CASCADE)
    fk_sanidade = models.OneToOneField(SanidadeBar, on_delete=models.CASCADE, blank=True)
    fk_ocultismo = models.OneToOneField(OcultismoBar, on_delete=models.CASCADE, blank=True)
    fk_esforco = models.OneToOneField(EsforcoBar, on_delete=models.CASCADE)
    
    fk_atributos = models.OneToOneField(Atributos, on_delete=models.CASCADE)
    fk_pericias = models.OneToOneField(Pericias, on_delete=models.CASCADE, blank=True)
    fk_resistencias = models.OneToOneField(Resistencias, on_delete=models.CASCADE, blank=True)
    fk_antescendentes = models.OneToOneField(Antescendentes, on_delete=models.CASCADE, blank=True)
    fk_iventario = models.OneToOneField(Iventario, on_delete=models.CASCADE, blank=True)
    
    def __str__(self) -> str:
        return self.nome