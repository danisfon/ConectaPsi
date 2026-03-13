from django.db import models

# CLASSE DE TESTE
class Campus (models.Model) :
    nome = models.CharField(max_length=50)
    cadastrado_em = models.DateField(auto_now_add=True)
    atualizado_em = models.DateField(auto_now_add=True)
    cadastrado_por = models.ForeignKey(User, on_delete=models.PROTECT)

    #COMANDO PARA CRIAR O O APP: python manage.py startapp NOME_AQUI