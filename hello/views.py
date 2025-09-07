from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


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
  elif request.method == "GET":
    return JsonResponse({
      "info": "This is a POST endpoint for greeting users",
      "usage": "Send POST request with JSON: {'name': 'YourName'}",
      "example_response": {"message": "Hello, YourName!"}
    })
  else:
    return JsonResponse({"error": "Only GET and POST methods allowed"}, status=405)

