from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello Django!</h1>")


def profile(request):
    context = {"name": "Rock", "age": "39", "height": "175", "weight": "88"}
    return JsonResponse(context)
