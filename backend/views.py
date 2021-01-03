from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from .models import City, Headers


def index(request):
    cities = City.objects.all().values()
    header = Headers.objects.get(name='index_header')
    return render(request, 'index.html', {'city': cities, 'header': header})


def indexAjax(request):
    cities = City.objects.all().values()
    header = Headers.objects.get(name='index_header')
    return JsonResponse({'city': list(cities)})

