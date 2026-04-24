from django.db import models
from django.contrib.auth.models import User


class Especialidade(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']


class Paciente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.PROTECT)
    telefone = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    endereco = models.CharField(max_length=255)

    def __str__(self):
        return self.usuario.username


class Psicologo(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.PROTECT)
    crp = models.CharField(max_length=20)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.PROTECT)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return f"{self.usuario.username} ({self.crp})"


class HorarioDisponivel(models.Model):
    psicologo = models.ForeignKey(Psicologo, on_delete=models.PROTECT)
    data = models.DateField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.psicologo} - {self.data} {self.hora_inicio}"


class Agendamento(models.Model):
    STATUS_CHOICES = [
        ('solicitado', 'Solicitado'),
        ('confirmado', 'Confirmado'),
        ('cancelado', 'Cancelado'),
        ('concluido', 'Concluído'),
    ]

    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    psicologo = models.ForeignKey(Psicologo, on_delete=models.PROTECT)
    horario = models.OneToOneField(HorarioDisponivel, on_delete=models.PROTECT)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='solicitado')
    data_solicitacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.paciente} - {self.psicologo} ({self.status})"


class Atendimento(models.Model):
    agendamento = models.OneToOneField(Agendamento, on_delete=models.PROTECT)
    observacoes = models.TextField()
    data_realizacao = models.DateTimeField()

    def __str__(self):
        return f"Atendimento {self.agendamento.id}"