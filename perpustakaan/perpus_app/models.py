from django.db import models

class Kelompok(models.Model):
    nama = models.CharField(max_length=9)
    keterangan = models.TextField()
    def __str__(self):
        return self.nama

class Buku(models.Model):
    judul = models.CharField(max_length=50)
    penulis = models.CharField(max_length=100)
    Kelompok = models.ForeignKey(Kelompok, on_delete=models.CASCADE, null=True) #cascade itu semisalnya yang class kelompok dihapus, trus nama2 yang sama bakal keapus juga
    img = models.CharField(null=True, max_length=40)
    def __str__(self):
        return self.judul #biar outputnya cuma muncul judul aja yezh

class Koordinat(models.Model):
    nama = models.CharField(max_length=10000)
    koordinat = models.CharField(max_length=54)
    def __str__(self):
        return self.nama
# Create your models here.
