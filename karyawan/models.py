from django.db import models

# Create your models here.
class Pengumuman(models.Model):
    judul_pengumuman = models.CharField(max_length=45)
    tanggal = models.DateField()
    jam = models.TimeField()

