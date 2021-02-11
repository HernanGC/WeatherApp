from django.db import models
from backend.helpers import kelvinToCelsius

# Create your models here.


class LatestSearch(models.Model):
    city                = models.CharField(max_length=30)
    long                = models.IntegerField()
    lat                 = models.IntegerField()
    weather_main        = models.CharField(max_length=30)
    weather_description = models.CharField(max_length=30)
    weather_icon        = models.CharField(max_length=30)
    temperature         = models.IntegerField()
    feels_like          = models.IntegerField()
    temp_min            = models.IntegerField()
    temp_max            = models.IntegerField()
    pressure            = models.IntegerField()
    humidity            = models.IntegerField()
    visibility          = models.IntegerField()
    wind_speed          = models.IntegerField()
    wind_deg            = models.IntegerField()
    clouds              = models.IntegerField()

    def __str__(self):
        return f'{self.pk} - {self.city}'

    def setName(self, pkey, name):
        city = LatestSearch.objects.filter(pk=pkey)
        city.city = name

    def getName(self):
        return self.city

    def getId(self):
        return self.pk

    def setModalObj(self):
        self.setCelsiusTemperature()
        self.capitalize()
        self.temperature = f'Temperature\n {self.temperature}'
        self.feels_like  = f'Feels like {self.feels_like}'
        self.temp_max    = f'Min {self.temp_max}'
        self.temp_min    = f'Max {self.temp_min}'

    def getCelsiusTemperature(self):
        return round(kelvinToCelsius(self.temperature))
    
    def capitalize(self):
        self.weather_description = self.weather_description.capitalize()
    
    def setCelsiusTemperature(self):
        self.temperature = round(kelvinToCelsius(self.temperature))
        self.feels_like  = round(kelvinToCelsius(self.feels_like))
        self.temp_max    = round(kelvinToCelsius(self.temp_max))
        self.temp_min    = round(kelvinToCelsius(self.temp_min))



class FavouriteCity(models.Model):
    city = models.ForeignKey(LatestSearch, on_delete=models.CASCADE)
    added_at = models.TimeField

    def __str__(self):
        return f'{self.city.pk} - {self.city.city}'

    def getName(self):
        return self.city.city

    def getTemp(self):
        return self.city.temperature
    
    def getWeather(self):
        return self.city.weather_main

    def getIcon(self):
        return self.city.weather_icon

class City(models.Model):
    name                = models.ForeignKey(LatestSearch, on_delete=models.CASCADE, name='name', related_name='name')
    weather_main        = models.CharField(max_length=30)
    weather_description = models.CharField(max_length=30)
    weather_icon        = models.CharField(max_length=30)
    temperature         = models.CharField(max_length=30)
    feels_like          = models.CharField(max_length=30)
    temp_min            = models.CharField(max_length=30)
    temp_max            = models.CharField(max_length=30)

    def __str__(self):
        return self.city


class Headers(models.Model):
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=30)
    body = models.TextField(max_length=300)

    def __str__(self):
        return self.name

# class MostSearched(models.Model):

#     def __str__(self):
#         return f'{self.pk} - {self.city}'