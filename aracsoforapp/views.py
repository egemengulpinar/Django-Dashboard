from django.shortcuts import render,redirect
  #from . import forms da yazılabilir
from transferapp.forms import TransferForm
from musteriapp.forms import MusteriForm
from sirketapp.forms import SirketForm,ExampleForm,ExampleModelForm
from aracsoforapp.forms import AracSoforForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
# Create your views here.
def sofor_ekle(request):
    form = AracSoforForm(request.POST or None)
    
    
    if form.is_valid(): #makale formunda boş bir alan olursa tekrar başa döndürülür sayfa (en aşağıdaki return ile)
        sofor = form.save(commit=False)
          
       
        
          
          
        sofor.save()
        messages.success(request,"Şöför Ekleme Işlemi Başarıyla Oluşturuldu")
        return redirect("aracsoforapp:sofor_ekle")

    return render(request,"sofor_ekle.html",{"form":form})   