from django.contrib import admin
from .models import LatestSearch, City, Headers, FavouriteCity

# Register your models here.

models = (City, Headers, LatestSearch, FavouriteCity)

admin.site.register(models)
