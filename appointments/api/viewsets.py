# 1. Importa o motor principal: o ModelViewSet já vem com as funções 
# de Listar, Criar, Ver Detalhes, Editar e Deletar prontas.
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from django_filters.rest_framework import DjangoFilterBackend

from appointments.api import serializers

from appointments import models

@extend_schema(tags=['Agendamentos']) 
class Agendamentoviewsets(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, ) 
    serializer_class = serializers.AgendamentoSerializer
    queryset = models.Agendamento.objects.all()

    filter_backends = [
        DjangoFilterBackend,    
        filters.SearchFilter,  
        filters.OrderingFilter  
    ]
    
    # Filtrando através das chaves estrangeiras
    filterset_fields = ['cliente', 'serviço', 'data', 'status'] 
    
    # Buscando pelo texto do nome que está em outra tabela
    search_fields = ['cliente__nome', 'serviço__nome']
    
    # Ordenando por data ou pelo nome do cliente
    ordering_fields = ['data', 'cliente__nome']
    ordering = ['data'] 

@extend_schema(tags=['Clientes'])
class ClienteViewsets(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = serializers.ClienteSerializer 
    queryset = models.Cliente.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nome', 'email', 'cpf']
    ordering = ['nome']

@extend_schema(tags=['Serviços'])
class ServicoViewsets(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = serializers.ServiçoSerializer
    queryset = models.Serviço.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome', 'descricao']