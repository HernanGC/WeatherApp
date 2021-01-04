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
