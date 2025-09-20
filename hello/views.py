from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from django.shortcuts import render


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
  