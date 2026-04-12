from django.contrib import admin
from .models import Serviço, Cliente, Agendamento

@admin.register(Serviço)
class ServiçoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tempo', 'valor') # Colunas que aparecem na listagem
    search_fields = ('nome',) # Barra de busca por nome

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'serviço', 'data', 'hora', 'status')
    list_filter = ('status', 'data') # Filtros laterais por status e data
    search_fields = ('cliente__nome',) # Busca pelo nome do cliente (relacionamento)