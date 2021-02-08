from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse

import json, requests, logging, ast

from django.forms.models import model_to_dict
from .models import LatestSearch, City, Headers, FavouriteCity

from backend.helpers import prepareSearchData, getLastSearch

logger = logging.getLogger(__name__)


def index(request):
    cities = City.objects.all().values()
    favourite_cities = FavouriteCity.objects.all().order_by('-id')[:5]
    header = Headers.objects.get(name='index_header')
    latest_search = LatestSearch.objects.all().order_by('-id')[:5]
    return render(request, 'index.html', {
        'city': cities, 
        'header': header, 
        'latest_search': latest_search, 
        'favourite_cities': favourite_cities
        })


def searchRequest(request):
    if request.method == 'POST':
        # TODO: Hacer un helper que haga este decodeo
        input_data = request.body.decode('utf-8')

# TODO: FILTRAR EL POR LOS CAMPOS QUE YO NECESITO, PARA NO OBTENER EL OBJECTO COMPLETO, SOLO NECESITO ESTO ['city', 'weather_main', 'temperature', 'weather_icon']
        last_search = LatestSearch.objects.latest('id')
        print(model_to_dict(last_search))
        # fields_to_filter = ['pk', 'city', 'weather_main', 'temperature', 'weather_icon']
        if last_search.getName() == input_data.capitalize():
            return JsonResponse({'msg': 'success', 'body': getLastSearch(model_to_dict(last_search))})

        request_string = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={input_data}&appid=772f2d88cb1fd3a790d48a49eb3d0aed')
        request_dict = ast.literal_eval(request_string.text)
        if request_dict['cod'] == 200:
            new_search_object = prepareSearchData(request_dict)
            new_search = LatestSearch(**new_search_object['search_object'])
            new_search.save()
            return JsonResponse({'msg': 'success', 'body': new_search_object['result_object']})
        else:
            return JsonResponse({'msg': 'fail', 'body': request_dict['message']})
    else:
        return JsonResponse({'msg': 'fail', 'body': 'Wrong request, only post accepted'})


def ajaxLatestSearch(request):
    if request.method == 'POST':
        # TODO: Hacer un helper que haga este decodeo
        status = request.body.decode('utf-8')
        if status == 'success':
            latest_search = LatestSearch.objects.all().order_by('-id')[1:6].values()
        else:
            latest_search = LatestSearch.objects.all().order_by('-id')[:5].values()
        return JsonResponse({'latest_search': list(latest_search)})
    else:
        return JsonResponse({'msg': 'fallo'})


def getLastSearchObject():
    last_search = LatestSearch.objects.latest('id')


def ajaxGetSearchById(request):
    if request.method == 'POST':
        # TODO: Hacer un helper que haga este decodeo
        objectId = request.body.decode('utf-8').replace('"', '')
        latest_search = LatestSearch.objects.get(pk=int(objectId))
        print(latest_search)
        return JsonResponse({'msg': 'success', 'body': model_to_dict(latest_search)})
    else:
        return JsonResponse({'msg': 'fallo'})
