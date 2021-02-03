from django.db import models
from django.utils import timezone

class GonderiModel(models.Model):
    class Meta:
        verbose_name="Gönderi"
        verbose_name_plural = "Gönderiler"
    SECENEKLER = [("1","Korku"),("2","Komedi"),("3","Günlük")]
    tur = models.CharField(max_length=8,choices=SECENEKLER,default="1")
    baslik = models.CharField(verbose_name="Başlık",max_length=200)
    yazi = models.TextField(verbose_name="Yazı")
    kayitzaman = models.DateTimeField(verbose_name="Kayıt Tarih Saat",default=timezone.now)
    yayimzaman = models.DateTimeField(verbose_name="Yayın Zaman Tarih Saat",null=True,blank=True)

    def yayimla(self):
        self.yayimzaman = timezone.now()
        self.save()


    def __str__(self):
        return self.baslik