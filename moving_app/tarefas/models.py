from django.db import models

# Create your models here.


class Usuario(models.Model):
    chave_google = models.CharField(max_length=50, primary_key=True)
    xp = models.PositiveIntegerField(default=0)
    nivel = models.PositiveSmallIntegerField(default=1)


class Tarefa(models.Model):
    descricao = models.TextField()
    complete = models.BooleanField(default=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_create = models.DateField(auto_now_add=True)
    data_conclusao = models.DateField()
    data_concluded = models.DateField(null=True, blank=True)

