from django.db import models

from django.db.models import DateTimeField
from ckeditor.fields import RichTextField
from django.utils.timezone import now
# Create your models here.
class Sirket(models.Model):
    
    sirket_adi = models.CharField(max_length =50,verbose_name = "Şirket Adı",default="",blank=True)
    sirket_adresi = models.CharField(max_length=150,verbose_name="Şirket Adresi",default="",blank=True)
    sirket_no = models.CharField(max_length=20,verbose_name="Şirket Tel No",default="",blank=True)
    created_date = models.DateTimeField(verbose_name="Oluşturulma Tarihi",null=True)
    

   


    
    def __str__(self):
        return str(self.sirket_adi)
    class Meta:
        ordering=['-created_date']

class SirketCalisan(models.Model):
    sirket_bilgi = models.ForeignKey(Sirket,on_delete = models.CASCADE,verbose_name="Şirket Bilgisi",related_name ="sirket_bilgi",null=True)
    calisan_adi = models.CharField(max_length =50,verbose_name = "Çalışan Adı",default="",blank=True)
    calisan_soyad = models.CharField(max_length =50,verbose_name = "Çalışan Soyadı",default="",blank=True)
    calisan_TC_NO = models.CharField(max_length =12,null=True,verbose_name="Çalışan TC NO")
    calisan_ev_adresi = models.CharField(max_length=150,verbose_name ="Çalışan Ev Adresi",default="",blank=True)
    calisan_is_adresi = models.CharField(max_length=150,verbose_name ="Çalışan İş Adresi",default="",blank=True)
    calisan_tel_no = models.CharField(max_length=20,verbose_name="Çalışan Telefon No",default="",blank=True)
    created_date = models.DateTimeField(default=now , editable= True,blank=True,null=True,verbose_name="Oluşturulma Tarihi")

    def __str__(self):
        return str(self.calisan_adi)
    class Meta:
        ordering=['-created_date']
