from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .forms import TransferForm,ExampleForm
from musteriapp.forms import MusteriForm
from sirketapp.forms import SirketForm
from django.utils.timezone import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from .import views
from .models import Transfer
from sirketapp.models import Sirket
from musteriapp.models import Musteri
from django.contrib.auth.forms import PasswordChangeForm
from user.models import UserProfile
import pandas as pd
from .filters import TransferFilter
# Create your views here.

def transferler(request):
    pass

def index(request):
    context = {


    }
    return render(request,"index.html",context)

def kontrol_paneli(request):
    transferler = Transfer.objects.filer(author = request.user) 
    
    context ={
        "transferler" : transferler
    }
    return render(request,"kontrol_paneli.html",context)




def transfer_ekle(request):
    bos_tarih = None
    form = TransferForm(request.POST or None)
    form2 = ExampleForm(request.POST or None)
    ##INVALID YAPMAYI ÖĞREN:!!!!!!!!!!!!!!!!!! ?___!!!!!!!!!!!
    transferler = Transfer.objects.all()
    musteriler = Musteri.objects.all()
    
          

    if form.is_valid():
        
        
        transfer = form.save(commit=False)
        transfer.musteri_id = request.POST.get('Select')
        transfer.transfer_tarihi = form2["my_datetime_field"].value()  
        if transfer.transfer_tarihi == "":
            transfer.transfer_tarihi = bos_tarih
        transfer.save()
         #.save() yapınca hata vermekte.
        
       
        
        messages.success(request,"Transfer Ekleme Işlemi Başarıyla Oluşturuldu")
        return redirect("transferapp:index")
    
    return render(request,"transfer_ekle.html",{"form":form,"transferler":transferler,"musteriler":musteriler,"example_form":form2})



       
def dashboard(request):

   
    keyword = request.GET.get("keyword")
    
    


    if keyword:
        
        transferler = Transfer.objects.filter(musteri__ad_soyad__contains = keyword)
        #(user = request.user)
        sirketler =Sirket.objects.all()
        myFilter = TransferFilter(request.GET,queryset=transferler)
        transferler = myFilter.qs
        if transferler:
            return render(request,"dist/tables.html",{"sirketler":sirketler,"transferler":transferler,"myFilter":myFilter})
        
        if sirketler:
            try:
                sirketler =Sirket.objects.filter(sirket_adi__contains = keyword)
                for value in range(0,len(sirketler)): #bulunan şirketler kadar döngüye alıp tüm değerleri transferler değişkenine aktarılır.
                    transferler2 = Transfer.objects.filter(musteri__sirket_bilgisi_id = sirketler.values("id")[value].get("id")) #sirketlerdeki id sözlüğü içindeki id değerini alabilmek için bu yöntem uygulanır.
                    transferler = transferler2 | transferler #QuerySet Merge(Birleştirme) yapmak için  | operatörü kullanılır.
            except Sirket.DoesNotExist: #eğer bir nesne bulamzsa iki parametreyi içini boş doldurup return ederek hata almayı önlüyoruz.Çıktıda "transfer henüz bulunmuyor yazmakta"
                transferler = None
                sirketler = None
                return render(request,"dist/tables.html",{"sirketler":sirketler,"transferler":transferler,"myFilter":myFilter})
            
            return render(request,"dist/tables.html",{"sirketler":sirketler,"transferler":transferler,"myFilter":myFilter})
                    


            
            
           
    
        
    transferler = Transfer.objects.all() 
    sirketler =Sirket.objects.all()

    myFilter = TransferFilter(request.GET,queryset=transferler)
    transferler = myFilter.qs
    return render(request,"dist/tables.html",{"transferler":transferler,"sirketler":sirketler,"myFilter":myFilter})

def detail(request,id):
    transferler = get_object_or_404(Transfer,id = id)
    
    #yalnızca transferleri alarak sirket detaylarına da ulaşabiliriz.
    return render(request,"transfer_detay.html",{"transferler":transferler})
    
def deleteTransfer(request,id):
    transfer = get_object_or_404(Transfer,id=id)
    transfer.delete()

    messages.success(request,"Transfer Başarıyla Tablodan Silindi")

    return redirect("transferapp:kontrol_paneli")

def updateTransfer(request,id):
    transfer = get_object_or_404(Transfer, id = id)
    form = TransferForm(request.POST or None,instance = transfer) 
    if form.is_valid():
        transfer = form.save()
        #sirket bilgisi formda veriliyor.
        transfer.save()
        messages.success(request,"Transfer Ekleme Işlemi Başarıyla Oluşturuldu")
        return redirect("transferapp:index")

    return render(request,"update.html",{"form":form})      

def profile(request):
   
   
    user = UserProfile.objects.all()
    return render(request,"profile.html",{"user":user})

def musteri_detail(request,id):
    transferler = get_object_or_404(Transfer,id = id)
    
    #yalnızca transferleri alarak sirket detaylarına da ulaşabiliriz.
    return render(request,"musteri.html",{"transferler":transferler})    

def sirket_detail(request,id):
    transferler = get_object_or_404(Transfer,id = id)
    
    #yalnızca transferleri alarak sirket detaylarına da ulaşabiliriz.
    return render(request,"sirket.html",{"transferler":transferler})    

