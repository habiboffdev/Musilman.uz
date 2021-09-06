from django.contrib import admin
from .models import Sura,Ayah
import requests
# Register your models here.
admin.site.register(Sura)

admin.site.register(Ayah)