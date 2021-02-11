from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.forms.models import model_to_dict

import json, requests, logging, ast

from .models import LatestSearch, City, Headers, FavouriteCity
from backend.helpers import handleSearchData, decodeRequestBody



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


def ajaxSearchRequest(request):
    if request.method == 'POST':
        input_data = decodeRequestBody(request.body)
        last_search = getLastModelObjectById()
        if last_search.getName() == input_data.capitalize():
            return JsonResponse({'msg': 'success', 'body': model_to_dict(last_search)})
        request_string = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={input_data}&appid=772f2d88cb1fd3a790d48a49eb3d0aed')
        request_dict = ast.literal_eval(request_string.text)
        if request_dict['cod'] == 200:
            new_search_object = handleSearchData(request_dict)
            new_search = LatestSearch(**new_search_object)
            new_search.save()
            latestObject = getLastModelObjectById()
            return JsonResponse({'msg': 'success', 'body': model_to_dict(latestObject)})
        else:
            return JsonResponse({'msg': 'fail', 'body': request_dict['message']})
    else:
        return JsonResponse({'msg': 'fail', 'body': 'Wrong request, only post accepted'})


def ajaxLatestSearch(request):
    if request.method == 'POST':
        status = decodeRequestBody(request.body)
        if status == 'success':
            latest_search = LatestSearch.objects.all().order_by('-id')[1:6].values()
        else:
            latest_search = LatestSearch.objects.all().order_by('-id')[:5].values()
        return JsonResponse({'latest_search': list(latest_search)})
    else:
        return JsonResponse({'msg': 'fail', 'body': 'Wrong request method'})


def getLastSearchObject():
    last_search = LatestSearch.objects.latest('id')


def ajaxGetSearchById(request):
    if request.method == 'POST':
        objectId = decodeRequestBody(request.body)
        try:
            latest_search = LatestSearch.objects.get(pk=int(objectId))
            latest_search.setModalObj()
            return JsonResponse({'msg': 'success', 'body': model_to_dict(latest_search)})
        except:
            return JsonResponse({'msg': 'fail', 'body': 'Wrong id given'})
    else:
        return JsonResponse({'msg': 'fail', 'body': 'Wrong request method'})


def getModelObjectById():
    return LatestSearch.objects.get(pk=id)


def getLastModelObjectById():
    return LatestSearch.objects.latest('id')