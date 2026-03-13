from django.db import models

# CLASSE DE TESTE
class Campus (models.Model) :
    nome = models.CharField(max_length=50)
    cadastrado_em = models.DateField(auto_now_add=True)
    atualizado_em = models.DateField(auto_now_add=True)
