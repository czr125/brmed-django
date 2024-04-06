from django.urls import path
from app_brmed import views

urlpatterns = [
    # rota, view responsavel, nome de referencia 
    #brmed.com
    path('',views.home,name='home'),
    #brmed.com/cadastro
    path('usuarios/', views.usuarios,name='listagem_usuarios')
]   
