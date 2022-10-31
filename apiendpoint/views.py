from operator import truediv
from django.http import JsonResponse

def home(request):
    
    return JsonResponse({"slackUsername": "Sang", "backend": truediv, "age": 65, "bio": "I am a backend engineer"})