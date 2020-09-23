from django.shortcuts import render,redirect
from sirketapp.models import Sirket,SirketCalisan
  #from . import forms da yazılabilir
from transferapp.forms import TransferForm
from musteriapp.forms import MusteriForm
from sirketapp.forms import SirketForm,ExampleForm,ExampleModelForm,SirketCalisanForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
# Create your views here.
def sirket_ekle(request):
    form = SirketForm(request.POST or None)
    bos_isim = "Bireysel"
    form2 = ExampleForm(request.POST or None)
    if form.is_valid(): #makale formunda boş bir alan olursa tekrar başa döndürülür sayfa (en aşağıdaki return ile)
        sirket = form.save(commit=False)
        sirket.created_date = form2["my_datetime_field"].value()  
       # sirket.user = request.user
        if sirket.sirket_adi == "" :
          sirket.sirket_adi = "Bireysel"
          
        sirket.save()
        messages.success(request,"Şirket Ekleme Işlemi Başarıyla Oluşturuldu")
        return redirect("sirketapp:sirket_ekle")

    return render(request,"sirket_ekle.html",{"form":form,"example_form":form2})   


def sirket_eleman_ekle(request):
    form = SirketCalisanForm(request.POST or None)
    sirketler = Sirket.objects.all()
    form2 = SirketForm(request.POST or None)
    if form.is_valid(): #makale formunda boş bir alan olursa tekrar başa döndürülür sayfa (en aşağıdaki return ile)
        sirket_eleman = form.save(commit=False)
        sirket_eleman.sirket_bilgi_id = request.POST.get('Select_Sirket5') 
       
        
          
          
        sirket_eleman.save()
        messages.success(request,"Şirket Elemanı Ekleme Işlemi Başarıyla Oluşturuldu")
        return redirect("sirketapp:sirket_eleman_ekle")

    return render(request,"calisan_ekle.html",{"form":form,"sirketler":sirketler})       