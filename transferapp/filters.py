import django_filters
from django_filters import DateFilter
from django import forms

from .models import *
from musteriapp.models import Musteri

class DateInput(forms.DateInput):
    input_type = 'date'  # saatte istenirse datetime-local yap paşam.


class DateInput2(forms.DateInput):
    input_type = 'date'  # saatte istenirse datetime-local yap paşam.
class TransferFilter(django_filters.FilterSet):
    start_date = DateFilter(widget=DateInput,field_name="transfer_tarihi",lookup_expr="gte",label="Tarihinden İtibaren")
    end_date = DateFilter(widget=DateInput,field_name="transfer_tarihi",lookup_expr="lte",label="Tarihinden Önce")



#############################       sirket bilgisi eklenecek.
    class Meta:
        model = Transfer
        fields = ["musteri__sirket_bilgisi","transfer_ucreti","musteri__adi","musteri__soyad"]
       

class TarihFilter(django_filters.FilterSet):

    start_date2 = DateFilter(widget=DateInput2,field_name="transfer_tarihi",lookup_expr="gte",label="Tarihinden İtibaren")
    end_date2 = DateFilter(widget=DateInput2,field_name="transfer_tarihi",lookup_expr="lte",label="Tarihinden Önce")

    class Meta:
        model = Transfer
        fields = []  