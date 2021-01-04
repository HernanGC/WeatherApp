from django.contrib import admin
from .models import LatestSearch, City, Headers

# Register your models here.

models = (City, Headers, LatestSearch)

admin.site.register(models)
