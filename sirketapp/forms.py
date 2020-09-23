from django import forms
from .models import Sirket,SirketCalisan



class SirketForm(forms.ModelForm): #MODEL FORM İLE KISA YOLDAN ÜRETME
    class Meta:
        
        model = Sirket 
        fields = ["sirket_adi","sirket_adresi","sirket_no"]

class SirketCalisanForm(forms.ModelForm):
    class Meta:
        model = SirketCalisan
        fields = ["calisan_adi","calisan_soyad","calisan_ev_adresi","calisan_tel_no","calisan_TC_NO"]


class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'



class ExampleForm(forms.Form):
   
    my_datetime_field = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local','title': 'Deneme'}),label="Oluşturma Tarihi")


    fields = ["my_datetime_field"] 

class ExampleModelForm(forms.Form):
    class Meta:
        widgets = {'my_date_field' : DateInput()}            