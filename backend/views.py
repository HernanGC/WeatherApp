from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from .models import City, Headers

#class requestHandlerView(View):
 #   def get(self, request):
        #do_something()


def index(request):
    cities = City.objects.all().values()
    header = Headers.objects.get(name='index_header')
    return render(request, 'index.html', {'city': cities, 'header': header})


def indexAjax(request):
    cityy = request.POST.get('city').capitalize()
    if cityy:
        cities = list(City.objects.filter(city=cityy).values())
        if cities:
            citeis = cities
        else: 
            citeis = 'City not found'
    header = Headers.objects.get(name='index_header')
    #res['hg'] = append('okxD!')
    return JsonResponse({'city': citeis})

