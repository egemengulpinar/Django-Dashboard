from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .forms import TransferForm,ExampleForm
from musteriapp.forms import MusteriForm,MusteriAdresForm,MusteriAdres_Birakildigi_Form,MusteriForm2
from aracsoforapp.forms import AracSoforForm,AracForm
from sirketapp.forms import SirketForm,SirketCalisanForm
from django.utils.timezone import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from .import views
from aracsoforapp.models import AracModel,AracSofor
from .models import Transfer
from sirketapp.models import Sirket,SirketCalisan
from musteriapp.models import Musteri
from django.contrib.auth.forms import PasswordChangeForm
from user.models import UserProfile
import pandas as pd
from .filters import TransferFilter,TarihFilter
# Create your views here.

def transferler(request):
    pass

def index(request):
    context = {


    }
    return render(request,"dist/index_main.html",context)


def deneme1(request):
    sirketler = Sirket.objects.all()
    secili_sirket= ""
    for i in range(0,len(sirketler)):
        secili_sirket = Sirket.objects.filter().values("sirket_adi")[i].get("sirket_adi") + " " + secili_sirket
    
    uzunluk = len(sirketler)
    # mevcut_sirket = Sirket.objects.filter(sirket_adi__contains = "Bireysel").values("id")[0].get("id")      
    calisanlar = SirketCalisan.objects.all()
    donenkisi = request.POST.get('select2')
    

    return render(request,"deneme.html",{"sirketler":sirketler,"calisanlar":calisanlar,"uzunluk":uzunluk,"secili_sirket":secili_sirket})    

def kontrol_paneli(request):
    transferler = Transfer.objects.filer(author = request.user) 
    
    context ={
        "transferler" : transferler
    }
    return render(request,"kontrol_paneli.html",context)




def transfer_ekle(request):
    bos_tarih = None

    soforler = AracSofor.objects.all()
    sirketler = Sirket.objects.all()
    form = TransferForm(request.POST or None)
    form1 = MusteriForm(request.POST or None)
    form8 = MusteriForm2(request.POST or None)
    form2 = ExampleForm(request.POST or None)
    form3 = AracForm(request.POST or None)
    form4 = AracSoforForm(request.POST or None) 
    form_adres = MusteriAdresForm(request.POST or None)
    form_adres_birakildigi = MusteriAdres_Birakildigi_Form(request.POST or None)
    new_sirket = SirketForm(request.POST or None)
    ##INVALID YAPMAYI ÖĞREN:!!!!!!!!!!!!!!!!!! 
    transferler = Transfer.objects.all()
    musteriler = Musteri.objects.all()
    mevcut_sirket = Sirket.objects.filter(sirket_adi__contains = "Bireysel")
    sirket_form = request.POST.get('select1')
    sirket_calisan = SirketCalisan.objects.all() 
    calisan_var_mi = SirketCalisan.objects.filter(id = request.POST.get('select2'))        
    

        
    if form1.is_valid():
        
        musteri = form1.save(commit=False)
        
        if sirket_form:
            musteri.sirket_bilgisi_id = request.POST.get('select1')
            calisan =  SirketCalisan.objects.filter(id = request.POST.get('select2'))
            musteri.adi = calisan.values("calisan_adi")
            musteri.soyad = calisan.values("calisan_soyad")
            musteri.tel_no = calisan.values("calisan_tel_no")
            musteri.TC_NO = calisan.values("calisan_TC_NO")
            #eleman adını falan buraya gir       
        else:      
            if musteri.sirket_bilgisi_id == None :
                

                if not mevcut_sirket:
                    if new_sirket.is_valid():
                        sirket = new_sirket.save()
                        sirket.sirket_adi = "Bireysel"
                        sirket.sirket_adresi =""
                        sirket.sirket_no = ""
                        sirket.save()
                        musteri.sirket_bilgisi_id = sirket.id
                else:
                    mevcut_sirket = Sirket.objects.filter(sirket_adi__contains = "Bireysel").values("id")[0].get("id")          
                    musteri.sirket_bilgisi_id = mevcut_sirket

            
            

            
            
        musteri.is_adresi = form_adres["is_adresi"].value()
        musteri.ev_adresi = form_adres["ev_adresi"].value()
        if(musteri.is_adresi == ""):
            musteri.alindigi_adres = musteri.ev_adresi
        if(musteri.ev_adresi == ""):
            musteri.alindigi_adres = musteri.is_adresi
        if(musteri.ev_adresi == "" and musteri.is_adresi == ""):
            musteri.alindigi_adres = "Havaalanı"  
            musteri.is_adresi ="Havaalanı"

        musteri.birakildigi_is_adresi = form_adres_birakildigi["birakildigi_is_adresi"].value()
        musteri.birakildigi_ev_adresi = form_adres_birakildigi["birakildigi_ev_adresi"].value()

        
        if (musteri.birakildigi_is_adresi == ""):
            musteri.birakildigi_adres = musteri.birakildigi_ev_adresi
        if (musteri.birakildigi_ev_adresi == ""):
            musteri.birakildigi_adres = musteri.birakildigi_is_adresi
        if (musteri.birakildigi_is_adresi == "" and musteri.birakildigi_ev_adresi == ""):
            musteri.birakildigi_adres = "Havaalanı"
            musteri.birakildigi_is_adresi ="Havaalanı"

        if musteri.alindigi_adres == "Havaalanı" and musteri.birakildigi_adres =="Havaalanı":
            musteri.alindigi_adres = ""
            musteri.birakildigi_adres = ""
            musteri.birakildigi_is_adresi = ""
            musteri.is_adresi = ""

        musteri.save()
            
    if form8.is_valid():
        if sirket_form:

            musteri = form8.save(commit=False)
            
            if sirket_form:
                musteri.sirket_bilgisi_id = request.POST.get('select1')
                calisan =  SirketCalisan.objects.filter(id = request.POST.get('select2'))
                musteri.adi = calisan.values("calisan_adi")
                musteri.soyad = calisan.values("calisan_soyad")
                musteri.tel_no = calisan.values("calisan_tel_no")
                musteri.TC_NO = calisan.values("calisan_TC_NO")
                #eleman adını falan buraya gir       
            else:      
                if musteri.sirket_bilgisi_id == None :
                    

                    if not mevcut_sirket:
                        if new_sirket.is_valid():
                            sirket = new_sirket.save()
                            sirket.sirket_adi = "Bireysel"
                            sirket.sirket_adresi =""
                            sirket.sirket_no = ""
                            sirket.save()
                            musteri.sirket_bilgisi_id = sirket.id
                    else:
                        mevcut_sirket = Sirket.objects.filter(sirket_adi__contains = "Bireysel").values("id")[0].get("id")          
                        musteri.sirket_bilgisi_id = mevcut_sirket

                
                

                
                
            musteri.is_adresi = form_adres["is_adresi"].value()
            musteri.ev_adresi = form_adres["ev_adresi"].value()
            if(musteri.is_adresi == ""):
                musteri.alindigi_adres = musteri.ev_adresi
            if(musteri.ev_adresi == ""):
                musteri.alindigi_adres = musteri.is_adresi
            if(musteri.ev_adresi == "" and musteri.is_adresi == ""):
                musteri.alindigi_adres = "Havaalanı"  
                musteri.is_adresi ="Havaalanı"

            musteri.birakildigi_is_adresi = form_adres_birakildigi["birakildigi_is_adresi"].value()
            musteri.birakildigi_ev_adresi = form_adres_birakildigi["birakildigi_ev_adresi"].value()

            
            if (musteri.birakildigi_is_adresi == ""):
                musteri.birakildigi_adres = musteri.birakildigi_ev_adresi
            if (musteri.birakildigi_ev_adresi == ""):
                musteri.birakildigi_adres = musteri.birakildigi_is_adresi
            if (musteri.birakildigi_is_adresi == "" and musteri.birakildigi_ev_adresi == ""):
                musteri.birakildigi_adres = "Havaalanı"
                musteri.birakildigi_is_adresi ="Havaalanı"

            if musteri.alindigi_adres == "Havaalanı" and musteri.birakildigi_adres =="Havaalanı":
                musteri.alindigi_adres = ""
                musteri.birakildigi_adres = ""
                musteri.birakildigi_is_adresi = ""
                musteri.is_adresi = ""

            musteri.save()

    if form3.is_valid():
        arac = form3.save()
        arac.save()
        
   

 
    if form.is_valid():
        
        # transfer.musteri_id = request.POST.get('Select')
        transfer = form.save(commit=False)
        transfer.musteri_id = musteri.id
        transfer.arac_id = arac.id
        if request.POST.get('Select'):
             transfer.sofor_id = request.POST.get('Select')

        elif request.POST.get('Select2'):
            transfer.sofor_id = request.POST.get('Select2')

        
         #if value "no ise ... yap"
        #transfer.musteri.sirket_bilgisi_id = request.POST.get('Select') #if value "no ise ... yap"
        transfer.transfer_tarihi = form2["my_datetime_field"].value()  
        if transfer.transfer_tarihi == "":
            transfer.transfer_tarihi = bos_tarih
        transfer.save()
         #.save() yapınca hata vermekte.
        
       
        
        messages.success(request,"Transfer Ekleme Işlemi Başarıyla Oluşturuldu")
        return redirect("transferapp:transfer_ekle")
    
    return render(request,"transfer_ekle.html",{"form":form,"transferler":transferler,"musteriler":musteriler,"example_form":form2,"form3":form3,"form1":form1,"form_adres":form_adres,"soforler":soforler,"sirketler":sirketler,"form_adres_birakildigi":form_adres_birakildigi,"sirket_calisan":sirket_calisan,"form8":form8})

def main_dashboard(request):
    
    keyword = request.GET.get("keyword")   
    transferler = Transfer.objects.all()
    transferler3 = Transfer.objects.all()   ### Ana paneldeki Toplam aylık-yıllık tutar para ve filtresi için
    toplam_para = 0
    toplam_para2 = 0
    toplam_para_yillik = 0
    kdv_dahil_toplam_para = 0
    if keyword:
        transferler2 = Transfer.objects.filter(musteri__sirket_bilgisi__sirket_adi__contains = keyword)
        transferler = Transfer.objects.filter(musteri__adi__contains = keyword)
        transferler4 = Transfer.objects.filter(musteri__soyad__contains = keyword)
        transferler5 = Transfer.objects.filter(musteri__alindigi_adres__contains = keyword)
        transferler6 = Transfer.objects.filter(musteri__birakildigi_adres__contains = keyword)
        transferler7 = Transfer.objects.filter(musteri__TC_NO__contains = keyword)
        transferler8 = Transfer.objects.filter(musteri__tel_no__contains = keyword)
        transferler9 = Transfer.objects.filter(transfer_ucreti__contains = keyword)
        transferler10 = Transfer.objects.filter(arac__arac_plaka__contains = keyword)
        transferler11 = Transfer.objects.filter(sofor__sofor_adi__contains = keyword)
        transferler = transferler | transferler2 #merge(birleştirme yapmak) Kısa yolu ? ?
        transferler = transferler | transferler4
        transferler = transferler | transferler5
        transferler = transferler | transferler6
        transferler = transferler | transferler7
        transferler = transferler | transferler9 
        transferler = transferler | transferler10
        transferler = transferler | transferler11 
        toplam_para = 0
        toplam_para2 = 0
        toplam_para_yillik = 0
        kdv_dahil_toplam_para = 0
        
        for value in range(0,len(transferler)):
            toplam_para = toplam_para + transferler.values("transfer_ucreti")[value].get("transfer_ucreti")
        kdv_dahil_toplam_para = ((toplam_para * 18) / 100) + toplam_para
        myFilter = TransferFilter(request.GET,queryset=transferler)
        
    
        transferler = myFilter.qs 
        
        if not transferler:
            transferler = None
            
            toplam_para = None
            kdv_dahil_toplam_para = None
            return render(request,"dist/index.html",{"transferler":transferler,"myFilter":myFilter,"toplam_para":toplam_para,"kdv_dahil_toplam_para": kdv_dahil_toplam_para})
        if transferler:
            
            return render(request,"dist/index.html",{"transferler":transferler,"myFilter":myFilter,"toplam_para":toplam_para,"kdv_dahil_toplam_para": kdv_dahil_toplam_para})
   
    #(user = request.user)
    
    sirketler =Sirket.objects.all()
    myFilter = TransferFilter(request.GET,queryset=transferler)
    myFilter2 = TarihFilter(request.GET,queryset=transferler3)
    transferler = myFilter.qs 
    transferler3 = myFilter2.qs
    for value in range(0,len(transferler)):
        toplam_para = toplam_para + transferler.values("transfer_ucreti")[value].get("transfer_ucreti")
    kdv_dahil_toplam_para = ((toplam_para * 18) / 100) + toplam_para    
    for value in range(0,len(transferler3)):
        toplam_para2 = toplam_para2 + transferler3.values("transfer_ucreti")[value].get("transfer_ucreti")
    kdv_dahil_toplam_para2 = ((toplam_para2 * 18) / 100) + toplam_para2
    toplam_para_yillik = toplam_para2 * 12
    if transferler:
        return render(request,"dist/index.html",{"sirketler":sirketler,"transferler":transferler,"transferler3":transferler3,"myFilter":myFilter,"myFilter2":myFilter2,"toplam_para_yillik":toplam_para_yillik,"toplam_para":toplam_para,"toplam_para2":toplam_para2,"kdv_dahil_toplam_para": kdv_dahil_toplam_para,"kdv_dahil_toplam_para2": kdv_dahil_toplam_para2})
    
    transferler = Transfer.objects.all() 
    sirketler =Sirket.objects.all()

    myFilter = TransferFilter(request.GET,queryset=transferler)
    myFilter2 = TarihFilter(request.GET,queryset=transferler3)
    transferler = myFilter.qs
    transferler3 = myFilter2.qs
    return render(request,"dist/index.html",{"transferler":transferler,"transferler3":transferler3,"sirketler":sirketler,"myFilter":myFilter,"myFilter2":myFilter2,"toplam_para":toplam_para,"kdv_dahil_toplam_para": kdv_dahil_toplam_para})
   

       
def dashboard(request):

    keyword = request.GET.get("keyword")   
    transferler = Transfer.objects.all() 
    toplam_para = 0
    kdv_dahil_toplam_para = 0
    if keyword:
        transferler2 = Transfer.objects.filter(musteri__sirket_bilgisi__sirket_adi__contains = keyword)
        transferler = Transfer.objects.filter(musteri__adi__contains = keyword)
        transferler4 = Transfer.objects.filter(musteri__soyad__contains = keyword)
        transferler5 = Transfer.objects.filter(musteri__alindigi_adres__contains = keyword)
        transferler6 = Transfer.objects.filter(musteri__birakildigi_adres__contains = keyword)
        transferler7 = Transfer.objects.filter(musteri__TC_NO__contains = keyword)
        transferler8 = Transfer.objects.filter(musteri__tel_no__contains = keyword)
        transferler9 = Transfer.objects.filter(transfer_ucreti__contains = keyword)
        transferler10 = Transfer.objects.filter(arac__arac_plaka__contains = keyword)
        transferler11 = Transfer.objects.filter(sofor__sofor_adi__contains = keyword)
        transferler = transferler | transferler2 #merge(birleştirme yapmak) Kısa yolu ? ?
        transferler = transferler | transferler4
        transferler = transferler | transferler5
        transferler = transferler | transferler6
        transferler = transferler | transferler7
        transferler = transferler | transferler9 
        transferler = transferler | transferler10
        transferler = transferler | transferler11
        toplam_para = 0
        kdv_dahil_toplam_para = 0
        
        for value in range(0,len(transferler)):
            toplam_para = toplam_para + transferler.values("transfer_ucreti")[value].get("transfer_ucreti")
        kdv_dahil_toplam_para = ((toplam_para * 18) / 100) + toplam_para
        myFilter = TransferFilter(request.GET,queryset=transferler)
       
    
        transferler = myFilter.qs 
        
        if not transferler:
            transferler = None
            
            toplam_para = None
            kdv_dahil_toplam_para = None
            return render(request,"dist/tables.html",{"transferler":transferler,"myFilter":myFilter,"toplam_para":toplam_para,"kdv_dahil_toplam_para": kdv_dahil_toplam_para})
        if transferler:
            
            return render(request,"dist/tables.html",{"transferler":transferler,"myFilter":myFilter,"toplam_para":toplam_para,"kdv_dahil_toplam_para": kdv_dahil_toplam_para})
    


  
    
    
        
    
    #(user = request.user)
    sirketler =Sirket.objects.all()
    myFilter = TransferFilter(request.GET,queryset=transferler)
   
    transferler = myFilter.qs 
    for value in range(0,len(transferler)):
        toplam_para = toplam_para + transferler.values("transfer_ucreti")[value].get("transfer_ucreti")
    kdv_dahil_toplam_para = ((toplam_para * 18) / 100) + toplam_para
    if transferler:
        return render(request,"dist/tables.html",{"sirketler":sirketler,"transferler":transferler,"myFilter":myFilter,"toplam_para":toplam_para,"kdv_dahil_toplam_para": kdv_dahil_toplam_para})
    
    
                


            
    
       
           
    
        
    transferler = Transfer.objects.all() 
    sirketler =Sirket.objects.all()

    myFilter = TransferFilter(request.GET,queryset=transferler)
    
    transferler = myFilter.qs
    return render(request,"dist/tables.html",{"transferler":transferler,"sirketler":sirketler,"myFilter":myFilter,"toplam_para":toplam_para,"kdv_dahil_toplam_para": kdv_dahil_toplam_para})



def detail(request,id):
    transferler = get_object_or_404(Transfer,id = id)
    
    #yalnızca transferleri alarak sirket detaylarına da ulaşabiliriz.
    return render(request,"dist/layout-static.html",{"transferler":transferler})
    
def deleteTransfer(request,id):
    transfer = get_object_or_404(Transfer,id=id)
    musteri = get_object_or_404(Musteri, id = transfer.musteri_id)
    transfer.delete()
    musteri.delete()

    messages.info(request,"Transfer Başarıyla Tablodan Silindi")

    return redirect("transferapp:ana_kontrol_panel")

def updateTransfer(request,id):
    bos_tarih = None
    soforler = AracSofor.objects.all()
    transfer = get_object_or_404(Transfer, id = id)
    musteri = get_object_or_404(Musteri, id = transfer.musteri_id)
    tarih = transfer.transfer_tarihi
    
    musteriler = Musteri.objects.all()


    secilen_kisi = Musteri.objects.filter(id=transfer.musteri.id)[0]
    sirket_bilgisi = transfer.musteri.sirket_bilgisi

    form = TransferForm(request.POST or None,instance = transfer) 
    form1 = MusteriForm(request.POST or None,instance = musteri)
    form2 = ExampleForm(request.POST or None)
    
    form3 = AracForm(request.POST or None,instance = transfer)
    form4 = AracSoforForm(request.POST or None,instance = transfer.sofor)
    form_adres = MusteriAdresForm(request.POST or None,instance = musteri)
    form_adres_birakildigi = MusteriAdres_Birakildigi_Form(request.POST or None,instance=musteri)
    if form.is_valid():
        if form1.is_valid():
            musteri = form1.save()
            musteri.is_adresi = form_adres["is_adresi"].value()
            musteri.ev_adresi = form_adres["ev_adresi"].value()
            if(musteri.is_adresi == ""):
                musteri.alindigi_adres = musteri.ev_adresi
            if(musteri.ev_adresi == ""):
                musteri.alindigi_adres = musteri.is_adresi
            if(musteri.ev_adresi == "" and musteri.is_adresi == ""):
                musteri.alindigi_adres = "Havaalanı"  
                musteri.is_adresi ="Havaalanı"

            musteri.birakildigi_is_adresi = form_adres_birakildigi["birakildigi_is_adresi"].value()
            musteri.birakildigi_ev_adresi = form_adres_birakildigi["birakildigi_ev_adresi"].value()

            
            if (musteri.birakildigi_is_adresi == ""):
                musteri.birakildigi_adres = musteri.birakildigi_ev_adresi
            if (musteri.birakildigi_ev_adresi == ""):
                musteri.birakildigi_adres = musteri.birakildigi_is_adresi
            if (musteri.birakildigi_is_adresi == "" and musteri.birakildigi_ev_adresi == ""):
                musteri.birakildigi_adres = "Havaalanı"
                musteri.birakildigi_is_adresi = "Havaalanı"

        
            musteri.save()
            
        transfer = form.save()
        if request.POST.get('Select5'):
             transfer.sofor_id = request.POST.get('Select5')

        
        
            
         
        
        transfer.transfer_tarihi = form2["my_datetime_field"].value() 
        if transfer.transfer_tarihi == "":
            transfer.transfer_tarihi = bos_tarih
        #sirket bilgisi formda veriliyor. 
        ###gerekirse araç şöför ve araç formunu da ekle ? SOR.
        
        transfer.save()
        messages.success(request,"Transfer Güncelleme Işlemi Başarıyla Oluşturuldu")
        return redirect("transferapp:ana_kontrol_panel")

    return render(request,"update.html",{"form":form,"soforler":soforler,"transfer":transfer,"secilen_kisi":secilen_kisi,"sirket_bilgisi":sirket_bilgisi,"form1":form1,"example_form":form2,"form_adres":form_adres,"form_adres_birakildigi":form_adres_birakildigi,"form4":form4})      

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

def sofor_tablosu(request):
    
    table_sofor = AracSofor.objects.all()
    transferler = Transfer.objects.all()
    
       
    
    ##Message ekle silme işlemi için
    
    
    return render(request,"sofor_tablo.html",{"table_sofor":table_sofor,"transferler":transferler})
def sofor_tablo_delete(request,id):
    
    
    sofor = get_object_or_404(AracSofor,id=id)
    sofor.delete()
       
    messages.info(request,"Transfer Başarıyla Tablodan Silindi")   
    ##Message ekle silme işlemi için
    
    
    return redirect("transferapp:sofor_tablo")




def sirket_tablosu(request):
    
    sirketler = Sirket.objects.all()
    calisanlar = SirketCalisan.objects.all()
    
       
    
    ##Message ekle silme işlemi için
    
    
    return render(request,"sirket_tablo.html",{"sirketler":sirketler,"calisanlar":calisanlar})


def sirket_tablo_delete(request,id):
    
   
    sirket = get_object_or_404(Sirket,id=id)
    sirket.delete()
       
    messages.info(request,"Şirket Başarıyla Tablodan Silindi")   
    ##Message ekle silme işlemi için
    
    
    return redirect("transferapp:sirket_tablo")

def sirket_calisan_delete(request,id):
    calisan = get_object_or_404(SirketCalisan,id=id)
    calisan.delete()
       
    messages.info(request,"Çalışan Başarıyla Tablodan Silindi")   
    ##Message ekle silme işlemi için
    
    
    return redirect("transferapp:sirket_tablo")

def sofor_guncelle(request,id):
    
    mevcut_sofor = get_object_or_404(AracSofor, id = id)
    form4 = AracSoforForm(request.POST or None,instance = mevcut_sofor)
    if form4.is_valid():
        mevcut_sofor.sofor_adi = form4["sofor_adi"].value()
        mevcut_sofor.sofor_tel_no = form4["sofor_tel_no"].value()
        mevcut_sofor.save()
        messages.success(request,"Şöför Güncelleme Işlemi Başarıyla Oluşturuldu")
        return redirect("transferapp:sofor_tablo")    
        
    return render(request,"sofor_update.html",{"form4":form4})


def sirket_guncelle(request,id):
    
    mevcut_sirket = get_object_or_404(Sirket, id = id)
    form5 = SirketForm(request.POST or None,instance = mevcut_sirket)
    if form5.is_valid():
        mevcut_sirket.sofor_adi = form5["sirket_adi"].value()
        mevcut_sirket.sofor_adi = form5["sirket_adresi"].value()
        mevcut_sirket.sofor_tel_no = form5["sirket_no"].value()
        mevcut_sirket.save()
        messages.success(request,"Şirket Güncelleme Işlemi Başarıyla Oluşturuldu")
        return redirect("transferapp:sirket_tablo")    
        
    return render(request,"sirket_update.html",{"form5":form5})    



def sirket_eleman_guncelle(request,id):
    
    mevcut_sirket_eleman = get_object_or_404(SirketCalisan, id = id)
    form5 = SirketCalisanForm(request.POST or None,instance = mevcut_sirket_eleman)
    if form5.is_valid():
        
        mevcut_sirket_eleman.calisan_adi = form5["calisan_adi"].value()
        mevcut_sirket_eleman.calisan_soyad =form5["calisan_soyad"].value()
        mevcut_sirket_eleman.calisan_ev_adresi =form5["calisan_ev_adresi"].value()
        mevcut_sirket_eleman.calisan_tel_no = form5["calisan_tel_no"].value()
        mevcut_sirket_eleman.calisan_TC_NO =form5["calisan_TC_NO"].value()
        mevcut_sirket_eleman.save()
        messages.success(request,"Şirket Eleman Güncelleme Işlemi Başarıyla Oluşturuldu")
        return redirect("transferapp:sirket_tablo")    
        
    return render(request,"sirket_eleman_update.html",{"form5":form5})      


"""
def uploadSmallFile(request):
    if request.POST or None:
        file = request.FILES.get('img')
        filename = file.name
        key = 'media/' + filename
        s3_resource = boto3.resource('s3')
        bucket = s3_resource.Bucket('sfm-aws-assets')
        bucket.put_object(Key=key, Body=file)
        if filename != '':
            volume, removed_volume = Methods.get_volume_info(key)
            #do something
        context = {'volume': volume, 'removed_volume': removed_volume}
        return JsonResponse(context)
"""  

"""
$.ajax({
    method: 'POST',
    url: '{% url 'data:smallUpload' %}',
    type: 'POST',
    contentType: false,
    processData: false,
    data: {'id': id},
}).done(function(data) {
    $("#id_rectangleRemovedVolume").val(data['removed_volume']);
    $("#id_rectangleVolume").val(data['volume']);
    loader.style.display = 'none';
    $("#id_Volume").val('');
}).fail(function(xhr, text, error) {
    console.log(text, error)
});
"""