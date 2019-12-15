from django.db import models

# Create your models here.

class Mahasiswa(models.Model):
    nim             =models.CharField(max_length=100)
    nama_depan      =models.CharField(max_length=100)
    nama_belakang   =models.CharField(max_length=100)
    prodi           =models.CharField(max_length=100)
    alamat           =models.CharField(max_length=100)
    
    def __str__(self):
        return "{}.{}".format(self.nim,self.nama_depan)
    