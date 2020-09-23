from django.contrib import admin
from django.urls import path
from .import views
from django.conf.urls import url
from user.models import UserProfile

app_name = "transferapp"

urlpatterns = [
    #yönlendirilen url'ler burada gözükmekte.
    path('kontrol_paneli/',views.dashboard,name = "kontrol_paneli" ),
    path('ana_kontrol_panel/',views.main_dashboard,name = "ana_kontrol_panel" ),
    path('transfer_ekle/',views.transfer_ekle,name = "transfer_ekle" ),
    path('musteri/<int:id>',views.musteri_detail,name = "musteri_detail" ),
    path('sirket/<int:id>',views.sirket_detail,name = "sirket_detail" ),
    path('profil_goruntule/',views.profile,name = "profil" ),
    path('transfer/<int:id>',views.detail,name = "detail" ),
    path('delete/<int:id>',views.deleteTransfer,name = "delete"),
    path('update/<int:id>',views.updateTransfer,name = "update"),
    path('', views.index, name = "index"),
    path('sofor_tablo/', views.sofor_tablosu, name = "sofor_tablo"),
    path('sofor_tablo_delete/<int:id>', views.sofor_tablo_delete, name = "sofor_tablo_delete"),
    path('sirket_tablo/', views.sirket_tablosu, name = "sirket_tablo"),
    path('sirket_tablo_delete/<int:id>', views.sirket_tablo_delete, name = "sirket_tablo_delete"),
    path('sofor_update/<int:id>',views.sofor_guncelle,name = "sofor_update"),    
    path('sirket_update/<int:id>',views.sirket_guncelle,name = "sirket_update"), 
    path('sirket_eleman_update/<int:id>',views.sirket_eleman_guncelle,name = "sirket_eleman_update"), 
    path('sirket_calisan_delete/<int:id>',views.sirket_calisan_delete,name = "sirket_calisan_delete"),
    path('deneme1/',views.deneme1,name = "deneme1" ),
    
]
