from django.contrib import admin
from .models import City, Headers

# Register your models here.

models = (City, Headers)

admin.site.register(models)
