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

    def getCelsiusTemperature(self):
        return round(kelvinToCelsius(self.temperature))

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
    city_fk             = models.ForeignKey(LatestSearch, on_delete=models.CASCADE)
    city_name           = models.CharField(default=city_fk.name)
    weather_main        = models.CharField(default='xd')
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