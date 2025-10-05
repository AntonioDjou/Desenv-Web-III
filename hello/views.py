from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from django.shortcuts import render

# Sistema de Login
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
  return HttpResponse("Hello, Django!")


def hello2(request, name):
  return HttpResponse(f"Hello, {name}!")

@csrf_exempt
def post_hello(request):
  if request.method == "POST":
    try:
      data = json.loads(request.body)
      name = data.get("name", "Guest")
      return JsonResponse({"message": f"Hello, {name}!"})
    except json.JSONDecodeError:
      return JsonResponse({"error": "Invalid JSON format"}, status=400)
  else:
    return JsonResponse({"error": "POST method required"}, status=405)

def inicial(request):
  return render(request, 'inicial.html')

def problema(request):
  return render(request, 'problema.html')

def solucao(request):
  return render(request, 'solucao.html')

def autor(request):
  return render(request, 'autor.html')

#Sistema de Login
def login_view(request):
  # Se o formulário foi enviado (método POST)
  if request.method == 'POST':
      # Pega o 'username' e a 'password' do formulário
      # Os nomes 'username' e 'password' devem ser os mesmos dos atributos 'name' nos inputs do seu HTML
      username_form = request.POST.get('username')
      password_form = request.POST.get('password')

      # Autentica o usuário com as credenciais fornecidas
      user = authenticate(request, username=username_form, password=password_form)

      # Verifica se a autenticação foi bem-sucedida
      if user is not None:
          # Se o usuário é válido, inicia a sessão para ele
          login(request, user)
          # Redireciona para a página principal do mapa do jogo após o login
          # Vamos criar essa página depois. Por enquanto, pode ser um redirect para '/'
          return redirect('mapa') # Usaremos um nome de URL para ser mais flexível
      else:
          # Se as credenciais forem inválidas, envia uma mensagem de erro
          messages.error(request, 'Login ou senha inválidos.')
          return redirect('login')

  # Se a requisição for GET, apenas mostra a página de login
  return render(request, 'login.html')

def logout_view(request):
  logout(request)
  messages.success(request, 'Você saiu da sua conta com sucesso!')
  return redirect('login')

# Futuramente, a view do mapa principal do seu jogo
def mapa_view(request):
  # Aqui você vai adicionar a lógica para mostrar o mapa, progresso do herói, etc.
  # Por enquanto, apenas uma página simples.
  return render(request, 'mapa.html')