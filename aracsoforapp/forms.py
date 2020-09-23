from django import forms
from .models import AracSofor,AracModel
from musteriapp.models import  Musteri
class AracSoforForm(forms.ModelForm): #MODEL FORM İLE KISA YOLDAN ÜRETME
    


    class Meta:
        model = AracSofor 
        fields = ["sofor_adi","sofor_tel_no"]

class AracForm(forms.ModelForm):

    class Meta:
        model = AracModel
        fields = ["arac_model","arac_plaka"]       