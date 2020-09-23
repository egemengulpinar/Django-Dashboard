from django.contrib import admin
from django.urls import path,include
from . import views

app_name = "sirketapp"
urlpatterns = [
    
     path('sirket_ekle/',views.sirket_ekle,name = "sirket_ekle" ),
     path('sirket_eleman_ekle/',views.sirket_eleman_ekle,name = "sirket_eleman_ekle" ),
    
]