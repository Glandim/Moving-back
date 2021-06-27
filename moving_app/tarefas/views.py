from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone

from moving_app.tarefas.models import Tarefa, Usuario
from moving_app.tarefas.serializers import TarefaSerializer


class TarefaListViewSet(generics.ListAPIView):
    serializer_class = TarefaSerializer
    model = Tarefa
    lookup_url_kwarg = "chave_google"
    
    def get_queryset(self):
        chave_google = self.kwargs.get(self.lookup_url_kwarg)
        usuario, _ = Usuario.objects.get_or_create(chave_google=chave_google)
        return Tarefa.objects.filter(usuario=usuario).order_by('complete')


class TarefaCreateViewSet(generics.CreateAPIView):

    serializer_class = TarefaSerializer

    def post(self, request, *args, **kwargs):
        data = {
            'descricao': request.data.get('descricao'),
            'usuario': request.data.get('usuario'),
            'data_conclusao': request.data.get('data_conclusao')
        }
        serializer = self.get_serializer_class()
        serializer = serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TarefaDeleteViewSet(generics.DestroyAPIView):
    queryset = Tarefa.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class TarefaUpdateViewSet(generics.UpdateAPIView):

    queryset = Tarefa.objects.all()

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.complete = True
        instance.data_concluded = timezone.now().date
        instance.save()
        return Response(status=status.HTTP_200_OK)
