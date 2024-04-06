from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    email = models.EmailField(max_length=255)
    cpf = models.IntegerField()
    telefone = models.IntegerField()
    idade = models.DateField()
    senha = models.CharField(max_length=20)

    