from django.contrib import admin
from django.urls import path,include
from . import views

app_name = "aracsoforapp"
urlpatterns = [
    
     path('sofor_ekle/',views.sofor_ekle,name = "sofor_ekle" ),
    
]