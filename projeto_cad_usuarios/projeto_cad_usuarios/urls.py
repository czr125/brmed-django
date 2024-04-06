from django.urls import path
from app_brmed import views

urlpatterns = [
    # rota, view responsavel, nome de referencia 
    #brmed.com
    path('',views.home,name='home'),
    #cadastro
    path('cadastro/',views.cadastro,name='cadastro'),
    #brmed.com/cadastro
    path('usuarios/', views.usuarios,name='listagem_usuarios'),
    #brmed.com/agendamento
    path('agendamento/', views.agendamento,name='agendamento')
]   
