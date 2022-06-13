from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect


def index(request):
    return HttpResponse("Страница приложения о машинах")


def names(request, car_name: str):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1> Статьи про знаменитые машины </h1><p>{car_name}</p>")


def cars_by_years(request, year):
    if int(year) > 2022:
        return redirect('main_page', permanent=True)
    return HttpResponse(f"<h1> В {year} были выпущены следующие автомобили</h1>")


def page_not_found(request, exception: Exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
