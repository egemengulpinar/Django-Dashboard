from django.contrib import admin
from .models import Transfer
from aracsoforapp.models import AracSofor,AracModel
from user.models import UserProfile
from musteriapp.models import Musteri
from sirketapp.models import Sirket,SirketCalisan

# Register your models here.

@admin.register(AracSofor)
class AracsoforAdmin(admin.ModelAdmin):
    list_display=["sofor_adi","sofor_tel_no"]
    
    search_fields = ["sofor_adi","sofor_tel_no"]
    
    list_filter=["created_date"]
    class Meta:
        model = AracSofor

@admin.register(AracModel)
class AracModelAdmin(admin.ModelAdmin):
    list_display=["arac_model","arac_plaka"]
    
    search_fields = ["arac_model","arac_plaka"]
    
    list_filter=["created_date"]
    class Meta:
        model = AracModel


@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    def musteri_soyad(self,obj):
        return obj.musteri.soyad
    def TC_NO(self,obj):
        return obj.musteri.TC_NO    
    def sirket_bilgisi(self,obj):
        return obj.musteri.sirket_bilgisi    
    list_display=['sirket_bilgisi','musteri',"musteri_soyad","transfer_tarihi","transfer_ucreti","sofor","arac","TC_NO"]
    
    search_fields = ["musteri__adi","musteri__soyad","transfer_ucreti","transfer_tarihi"]
    
    list_filter=["transfer_tarihi"]

   
    class Meta:
        model = Transfer


@admin.register(Musteri)
class MusteriAdmin(admin.ModelAdmin):

    list_display=["ucus_kodu","adi","soyad","tel_no","ev_adresi","is_adresi","TC_NO","created_date"]
    

    search_fields = ["sirket_bilgisi__sirket_adi","adi","soyad","is_adresi","ev_adresi","tel_no","created_date"]
    
    list_filter=["created_date"]

    class Meta:
        model = Musteri

@admin.register(Sirket)
class SirketAdmin(admin.ModelAdmin):

    list_display=["sirket_adi","sirket_adresi","sirket_no","created_date"]

    search_fields = ["sirket_adi","sirket_adresi","sirket_no","created_date"]
    
    list_filter=["created_date"]
    class Meta:
        model = Sirket

@admin.register(SirketCalisan)
class SirketCalisanAdmin(admin.ModelAdmin):

    list_display=["calisan_adi","calisan_soyad","calisan_ev_adresi","calisan_tel_no","calisan_TC_NO"]

    search_fields = ["calisan_adi","calisan_soyad","calisan_ev_adresi","calisan_tel_no","calisan_TC_NO"]
    
    list_filter=["created_date"]
    class Meta:
        model = SirketCalisan



@admin.register(UserProfile)
class UserAdmin(admin.ModelAdmin):


    list_display=["created_date","user"]
    search_fields = ["user","created_date"]
    list_filter = ["created_date"]

    class Meta:
        model = UserProfile        