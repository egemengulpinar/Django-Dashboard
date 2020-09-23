from django.db import models

from django.db.models import DateTimeField
from ckeditor.fields import RichTextField
from django.utils.timezone import now

class AracSofor(models.Model):
    
    
    ##ŞÖFÖR BİLGİSİ------------------------------------------------------------------------
    sofor_adi = models.CharField(max_length =50,verbose_name = "Şöför Adı",default="",blank=True)
    sofor_tel_no = models.CharField(max_length=20,verbose_name="Şöför Telefon No",default="",blank=True)
    created_date = models.DateTimeField(default=now,editable=True,verbose_name="Oluşturulma Tarihi",null=True)
    ##ARAÇ BİLGİSİ------------------------------------------------------------------------
    

    
    def __str__(self):
        return str(self.sofor_adi)
    class Meta:
        ordering=['-created_date']


class AracModel(models.Model):
    
    arac_model = models.CharField(max_length =50,verbose_name = "Araç Modeli",default="",blank=True)
    arac_plaka = models.CharField(max_length =50,verbose_name = "Araç Plaka",default="",blank=True)
    created_date = models.DateTimeField(default=now,editable=True,verbose_name="Oluşturulma Tarihi",null=True)

    def __str__(self):
        return str(self.arac_plaka)
    class Meta:
        ordering=['-created_date']
    
