from django.db import models
from django.contrib.auth.models import User

class Especialidade(models.Model):
    nome = models.CharField(
        max_length=100,
        unique=True
    )

    descricao = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']



class Paciente(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    cpf = models.CharField(
        max_length=14,
        unique=True
    )

    telefone = models.CharField(
        max_length=20
    )

    data_nascimento = models.DateField()

    endereco = models.CharField(
        max_length=255
    )

    cadastrado_em = models.DateTimeField(
        auto_now_add=True
    )

    atualizado_em = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        ordering = ['user__first_name']


class Profissional(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    especialidade = models.ForeignKey(
        Especialidade,
        on_delete=models.PROTECT,
        related_name="profissionais"
    )

    crp = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="CRP"
    )

    telefone = models.CharField(
        max_length=20
    )

    bio = models.TextField(
        verbose_name="Biografia",
        blank=True,
        null=True
    )

    ativo = models.BooleanField(
        default=True
    )

    cadastrado_em = models.DateTimeField(
        auto_now_add=True
    )

    atualizado_em = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.user.get_full_name()} ({self.crp})"

    class Meta:
        ordering = ['user__first_name']



class Agenda(models.Model):

    DIAS_SEMANA = (
        (1, "Segunda-feira"),
        (2, "Terça-feira"),
        (3, "Quarta-feira"),
        (4, "Quinta-feira"),
        (5, "Sexta-feira"),
        (6, "Sábado"),
        (7, "Domingo"),
    )

    profissional = models.ForeignKey(
        Profissional,
        on_delete=models.CASCADE,
        related_name="agendas"
    )

    dia_semana = models.PositiveSmallIntegerField(
        choices=DIAS_SEMANA
    )

    hora_inicio = models.TimeField()

    hora_fim = models.TimeField()

    ativo = models.BooleanField(
        default=True
    )

    def __str__(self):
        return f"{self.profissional} - {self.get_dia_semana_display()}"

    class Meta:
        ordering = ['dia_semana', 'hora_inicio']



class Consulta(models.Model):

    STATUS_CHOICES = (
        ("AGENDADA", "Agendada"),
        ("CONFIRMADA", "Confirmada"),
        ("CANCELADA", "Cancelada"),
        ("FINALIZADA", "Finalizada"),
    )

    paciente = models.ForeignKey(
        Paciente,
        on_delete=models.PROTECT,
        related_name="consultas"
    )

    profissional = models.ForeignKey(
        Profissional,
        on_delete=models.PROTECT,
        related_name="consultas"
    )

    data = models.DateField()

    hora = models.TimeField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="AGENDADA"
    )

    motivo = models.TextField(
        blank=True,
        null=True
    )

    observacoes = models.TextField(
        blank=True,
        null=True
    )

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    atualizado_em = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.paciente} - {self.data}"

    class Meta:
        ordering = ['-data', '-hora']



class Prontuario(models.Model):

    consulta = models.ForeignKey(
        Consulta,
        on_delete=models.CASCADE,
        related_name="prontuarios"
    )

    paciente = models.ForeignKey(
        Paciente,
        on_delete=models.PROTECT,
        related_name="prontuarios"
    )

    profissional = models.ForeignKey(
        Profissional,
        on_delete=models.PROTECT,
        related_name="prontuarios"
    )

    descricao = models.TextField()

    diagnostico = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    observacoes = models.TextField(
        blank=True,
        null=True
    )

    data_registro = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Prontuário #{self.pk}"

    class Meta:
        ordering = ['-data_registro']



class Pagamento(models.Model):

    STATUS_CHOICES = (
        ("PENDENTE", "Pendente"),
        ("PAGO", "Pago"),
        ("CANCELADO", "Cancelado"),
    )

    METODO_CHOICES = (
        ("PIX", "Pix"),
        ("CARTAO", "Cartão"),
        ("DINHEIRO", "Dinheiro"),
    )

    consulta = models.OneToOneField(
        Consulta,
        on_delete=models.CASCADE,
        related_name="pagamento"
    )

    valor = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    data_pagamento = models.DateField(
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="PENDENTE"
    )

    metodo = models.CharField(
        max_length=20,
        choices=METODO_CHOICES
    )

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Pagamento #{self.pk} - {self.status}"

    class Meta:
        ordering = ['-criado_em']