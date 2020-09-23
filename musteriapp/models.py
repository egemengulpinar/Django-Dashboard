from django.db import models
from sirketapp.models import Sirket
from user.models import UserProfile
from django.db.models import DateTimeField
from ckeditor.fields import RichTextField
from django.utils.timezone import now
# Create your models here.
class Musteri(models.Model):
   
    sirket_bilgisi = models.ForeignKey(Sirket,on_delete = models.CASCADE,verbose_name="Şirket Bilgisi",related_name ="sirket_bilgisi",null=True)
    adi = models.CharField(max_length =50,verbose_name = "Ad",null=True)
    soyad = models.CharField(max_length =50,verbose_name = "Soyad",null=True)
    is_adresi = models.CharField(max_length=150,verbose_name="İş Adresi",default="",blank=True)
    ev_adresi = models.CharField(max_length=150,verbose_name ="Ev Adresi",default="",blank=True)
    birakildigi_is_adresi = models.CharField(max_length=150,verbose_name ="Ev Adresi",default="",blank=True)
    birakildigi_ev_adresi = models.CharField(max_length=150,verbose_name ="Ev Adresi",default="",blank=True)
    alindigi_adres = models.CharField(max_length=150,verbose_name="Alındığı Adres",default="",null=True)
    birakildigi_adres = models.CharField(max_length=150,verbose_name ="Bırakıldığı Adres",default="",null=True)
    tel_no = models.CharField(max_length=20,verbose_name="Telefon No",null=True)
    created_date = models.DateTimeField(verbose_name="Oluşturulma Tarihi",null=True)
    ucus_kodu = models.CharField(max_length =50,verbose_name = "Ucuş Kodu",null=True)
    TC_NO = models.CharField(max_length =12,null=True,verbose_name="TC NO")
     
 
    def __str__(self):
        
        return '%s %s' % (self.adi,self.soyad) ##FİLTRE EKRANINDA  SELECT BOX İÇİNDE AD VE SOYAD GÖZÜKMESİ İÇİN BU ŞEKİLDE YAPILMAKTA.

    class Meta:
        ordering=['adi']