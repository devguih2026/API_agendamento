from rest_framework import serializers
from appointments.models import Serviço, Cliente, Agendamento

class ServiçoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Serviço
        fields = ['id', 'nome', 'tempo', 'valor']

class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = ['id', 'nome']

class AgendamentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Agendamento
        fields = "__all__"
