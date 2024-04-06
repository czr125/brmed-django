from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request, 'usuarios/home.html')

def cadastro(request):
    return render(request, 'usuarios/cadastro.html')

def usuarios(request):
    # Salvar os dados da tela para o banco de dados
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome_usuario')
    novo_usuario.email = request.POST.get('email_usuario')
    novo_usuario.cpf = request.POST.get('cpf_usuario')
    novo_usuario.telefone = request.POST.get('telefone_usuario')
    novo_usuario.idade = request.POST.get('idade_usuario')
    novo_usuario.senha = request.POST.get('senha_usuario')
    novo_usuario.save()

    # Exibir todos os usuarios cadastrados em uma nova página
    usuarios = {
        'usuarios':  Usuario.objects.all()
    }
    
    # Retornar os dados para a página de listagem
    return render(request,'usuarios/usuarios.html',usuarios)

def agendamento(request):
    return render(request, 'usuarios/agendamento.html')