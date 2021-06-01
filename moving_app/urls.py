from django.urls import include, path
from rest_framework import routers

from moving_app.tarefas import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/tarefas/create/', views.TarefaCreateViewSet.as_view(), name='tarefa-create'),
    path('api/tarefas/<int:pk>/delete/', views.TarefaDeleteViewSet.as_view(), name='tarefa-delete'),
    path('api/tarefas/<chave_google>/', views.TarefaListViewSet.as_view(), name='tarefa-list'),
    path('api/tarefas/<int:pk>/complete/', views.TarefaUpdateViewSet.as_view(), name='tarefa-update'),
]