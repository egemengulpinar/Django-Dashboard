from django import forms
from .models import Musteri



class MusteriForm(forms.ModelForm): #MODEL FORM İLE KISA YOLDAN ÜRETME

 #     ev_adresi = forms.CharField(
 #       required=False,
  #       widget = forms.Textarea(
 #            attrs={
 #                "placeholder": "Adresiniz",
 #                "class" : "form-control is-invalid",
  #               "id": "validationTextarea",
  #               "rows": 20,
   #              "cols":120
  #           }
  #       )
 #   )
 

    class Meta:
        model = Musteri 
        fields = ["ucus_kodu","adi","soyad","tel_no","TC_NO"]
        
class MusteriForm2(forms.ModelForm): #MODEL FORM İLE KISA YOLDAN ÜRETME

 #     ev_adresi = forms.CharField(
 #       required=False,
  #       widget = forms.Textarea(
 #            attrs={
 #                "placeholder": "Adresiniz",
 #                "class" : "form-control is-invalid",
  #               "id": "validationTextarea",
  #               "rows": 20,
   #              "cols":120
  #           }
  #       )
 #   )
 

    class Meta:
        model = Musteri 
        fields = ["ucus_kodu"]

class MusteriAdresForm(forms.ModelForm):
    ev_adresi = forms.CharField(
         label = "Alındığı Ev Adresi",
       required = False,
       widget = forms.Textarea(
           attrs={
               "blank":True,
               "placeholder": "Ev Adresi",
               "class" : "form-control ",
               "id": "validationTextarea",
               "rows": 3,
               "cols":10
           }
       )
    )
    is_adresi = forms.CharField(
         label = "Alındığı İş Adresi",
      required = False,
       widget = forms.Textarea(
           attrs={
               
               
               "placeholder": "İş Adresi",
               "class" : "form-control ",
               "id": "validationTextarea",
               "rows": 3,
               "cols":10
           }
       )
    )

    class Meta:
        model = Musteri 
        fields = ["ev_adresi","is_adresi"]


class MusteriAdres_Birakildigi_Form(forms.ModelForm):
    birakildigi_ev_adresi = forms.CharField(
        label = "Bırakıldığı Ev Adresi", 
       required = False,
       widget = forms.Textarea(
           attrs={
               "blank":True,
               "placeholder": "Ev Adresi",
               "class" : "form-control ",
               "id": "validationTextarea",
               "rows": 3,
               "cols":10
           }
       )
    )
    birakildigi_is_adresi = forms.CharField(
      required = False,
      label = "Bırakıldığı İş Adresi",
       widget = forms.Textarea(
           attrs={
               
               
               "placeholder": "İş Adresi",
               "class" : "form-control ",
               "id": "validationTextarea",
               "rows": 3,
               "cols":10
           }
       )
    )

    class Meta:
        model = Musteri 
        fields = ["birakildigi_ev_adresi","birakildigi_is_adresi"]