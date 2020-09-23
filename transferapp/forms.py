from django import forms
from .models import Transfer
from musteriapp.models import Musteri



class TransferForm(forms.ModelForm): #MODEL FORM İLE KISA YOLDAN ÜRETME


    transfer_ucreti = forms.CharField(
       
       widget = forms.Textarea(
           attrs={
               "placeholder": "Ücret",
               "class" : "form-control ",
               "id": "validationTextarea",
               "rows": 1,
               "cols":2
           }
       )
    )

    class Meta:
        model = Transfer 
        fields = ["transfer_ucreti"]
        
class ExampleForm(forms.Form):
   
    my_datetime_field = forms.DateTimeField(required=False,widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),label="Transfer Tarihi")

    
    fields = ["my_datetime_field"] 