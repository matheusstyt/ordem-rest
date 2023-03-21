# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from personagem.models import *


admin.site.register(Personagem)
admin.site.register(VidaBar)
admin.site.register(SanidadeBar)
admin.site.register(OcultismoBar)
admin.site.register(EsforcoBar)

admin.site.register(Armamento)
admin.site.register(Item)

admin.site.register(Atributo)
admin.site.register(Pericia)
admin.site.register(Resistencia)

admin.site.register(Atributos)
admin.site.register(Pericias)
admin.site.register(Resistencias)
admin.site.register(Iventario)

admin.site.register(Antescendente)
admin.site.register(Antescendentes)