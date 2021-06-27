from moving_app.tarefas.models import Tarefa
from rest_framework import serializers


class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = ['id', 'descricao', 'complete', 'usuario', 'data_create', 'data_conclusao', 'data_concluded']
