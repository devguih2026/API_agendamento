from django.urls import path, include
from rest_framework.routers import DefaultRouter
from appointments import views

# O Router cria automaticamente as rotas de GET, POST, PUT e DELETE
router = DefaultRouter()
router.register(r'agendamentos', views.Agendamentoviewsets, basename='agendamento')

urlpatterns = [
    path('', include(router.urls)),
]