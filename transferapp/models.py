from django.db import models
from musteriapp.models import Musteri
from aracsoforapp.models import AracSofor,AracModel
from django.db.models import DateTimeField
from ckeditor.fields import RichTextField
from django.utils.timezone import now
# Create your models here.

    
class Transfer(models.Model):
    #sirket_bilgisi = models.ForeignKey(UserProfile,on_delete = models.CASCADE,verbose_name="Şirket Bilgisi",related_name ="sirket_bilgisi",null=True)
    #transfer bilgisi related name ile transfer tablosuna erişim sağlanabilecek. Foreign Key iel bu bağlantı sağlanır.Devamında transfer_tarihi ve transfer_ucretine erişilebilir.
   
    #sirket_bilgisi = models.ForeignKey(Sirket,on_delete=models.CASCADE,verbose_name = "Şirket Bilgisi",related_name="sirket_bilgisi",null=True)
    musteri = models.ForeignKey(Musteri,on_delete = models.CASCADE,verbose_name="Müşteri",related_name ="musteri",null=True)
    arac = models.ForeignKey(AracModel,on_delete = models.CASCADE,verbose_name="Araç Modeli",related_name ="arac",null=True)
    sofor = models.ForeignKey(AracSofor,on_delete = models.CASCADE,verbose_name="Şöför",related_name ="sofor",null=True)
    transfer_tarihi = models.DateTimeField(default=now , editable= True,blank=True,null=True) #??
    transfer_ucreti = models.DecimalField(decimal_places =2,max_digits =10,null=True,verbose_name="Ücret")
    
   ######################ADRESI MUSTERIDEN ÇEK


    def __str__(self):
        return str(self.musteri.adi)
    class Meta:
        ordering=['-transfer_tarihi']

