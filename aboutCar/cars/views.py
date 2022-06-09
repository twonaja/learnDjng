from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Страница приложения о машинах")


def names(request, car_name: str):
    return HttpResponse(f"<h1> Статьи про знаменитые машины </h1><p>{car_name}</p>")
