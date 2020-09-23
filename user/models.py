from django.db import models

from django.db.models import DateTimeField
from ckeditor.fields import RichTextField
from django.utils.timezone import now
# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name="Kullanıcı",null=True)
    
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")

    def __str__(self):
        return self.user.username ##HATA ÇIKABİLİR
    class Meta:
        ordering=['-created_date']