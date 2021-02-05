from django.db import models

# Create your models here.


class LatestSearch(models.Model):
    city = models.CharField(max_length=30)
    long = models.IntegerField()
    lat = models.IntegerField()
    weather_main = models.CharField(max_length=30)
    weather_description = models.CharField(max_length=30)
    weather_icon = models.CharField(max_length=30)
    temperature = models.IntegerField()
    feels_like = models.IntegerField()
    temp_min = models.IntegerField()
    temp_max = models.IntegerField()
    pressure = models.IntegerField()
    humidity = models.IntegerField()
    visibility = models.IntegerField()
    wind_speed = models.IntegerField()
    wind_deg = models.IntegerField()
    clouds = models.IntegerField()

    def __str__(self):
        return f'{self.pk} - {self.city}'

    def setName(self, pkey, name):
        city = LatestSearch.objects.filter(pk=pkey)
        city.city = name

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
    city = models.CharField(max_length=30, blank=True)
    country = models.CharField(max_length=40)
    region = models.CharField(max_length=40)
    wheather = models.TextField(max_length=200)
    temperature = models.CharField(max_length=5)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

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