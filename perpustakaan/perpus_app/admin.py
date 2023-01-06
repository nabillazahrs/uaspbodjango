from django.contrib import admin

from .models import *
class bukuadmin(admin.ModelAdmin):
    list_display = ['judul', 'penulis','img']
    search_fields = ['judul', 'penulis']
    list_filter = ['Kelompok']
    list_per_page = 4

class koordinatadmin(admin.ModelAdmin):
    list_display = ['nama', 'koordinat']
    search_fields = ['nama']
    list_per_page = 5

admin.site.register(Buku, bukuadmin) #buat nambahin tabel di admin
admin.site.register(Kelompok)
admin.site.register(Koordinat, koordinatadmin)
# Register your models here.
