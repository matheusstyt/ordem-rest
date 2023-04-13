# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from personagem.models import *

admin.site.register(PerfilImage)
admin.site.register(Personagem)
admin.site.register(VidaBar)
admin.site.register(SanidadeBar)
admin.site.register(OcultismoBar)
admin.site.register(EsforcoBar)

admin.site.register(ArmamentosPersonagem)
admin.site.register(AcessoriosPersonagem)

admin.site.register(AtributosPersonagem)
admin.site.register(PericiasPersonagem)
admin.site.register(ResistenciasPersonagem)

admin.site.register(Iventario)

admin.site.register(AntescendentesPersonagem)
