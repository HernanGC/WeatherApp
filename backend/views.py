from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from .models import LatestSearch, City, Headers

#class requestHandlerView(View):
 #   def get(self, request):
        #do_something()


def index(request):
    cities = City.objects.all().values()
    header = Headers.objects.get(name='index_header')
    latest_search = LatestSearch.objects.all().order_by('-id')[:5]
    return render(request, 'index.html', {'city': cities, 'header': header, 'latest_search': latest_search})


def ajaxAddSearch(request):
    if request.method == 'POST':
        search = LatestSearch()
        search.city = request.POST.get('city')
        search.long = request.POST.get('long')
        search.lat = request.POST.get('lat')
        search.weather_main = request.POST.get('weather_main')
        search.weather_description = request.POST.get('weather_description')
        search.weather_icon = request.POST.get('weather_icon')
        search.temperature = request.POST.get('temperature')
        search.feels_like = request.POST.get('feels_like')
        search.temp_min = request.POST.get('temp_min')
        search.temp_max = request.POST.get('temp_max')
        search.pressure = request.POST.get('pressure')
        search.humidity = request.POST.get('humidity')
        search.visibility = request.POST.get('visibility')
        search.wind_speed = request.POST.get('wind_speed')
        search.wind_deg = request.POST.get('wind_deg')
        search.clouds = request.POST.get('clouds')
        search.save()
        return JsonResponse({'msg': 'success'})
    else:
        return JsonResponse({'msg': 'failed'})





# def indexAjax(request):
#     cityy = request.POST.get('city').capitalize()
#     if cityy:
#         cities = list(City.objects.filter(city=cityy).values())
#         if cities:
#             citeis = cities
#         else: 
#             citeis = 'City not found'
#     header = Headers.objects.get(name='index_header')
#     #res['hg'] = append('okxD!')
#     return JsonResponse({'city': citeis})

