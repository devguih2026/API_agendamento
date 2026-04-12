from django.db import models

class Serviço(models.Model):
    nome = models.CharField(max_length=150)
    tempo = models.DurationField() # minutos/horas que o serviço demora
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self):
        return self.nome

class Agendamento(models.Model):
    # Opções fixas para o status do agendamento
    STATUS = [
        ('P', 'Pendente'),
        ('C', 'Confirmado'),
        ('F', 'Finalizado'),
        ('X', 'Cancelado'),
    ]
    data = models.DateField()
    hora = models.TimeField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    serviço = models.ForeignKey(Serviço, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS, default='P')
    pagamento = models.CharField(max_length=150) # cartão ou pix
 


