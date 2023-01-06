from django.forms import ModelForm
from django import forms
from perpus_app.models import *

class FormBuku(ModelForm):
    class Meta:
        model = Buku
        fields = "__all__"

        widgets = {
            'judul' : forms.TextInput({'class': 'form-control','placeholder': 'Judul', 'required' : 'required' }),
            'penulis' : forms.TextInput({'class': 'form-control','placeholder': 'Penulis', 'required' : 'required' }),
            'kelompok' : forms.TextInput({'class': 'form-control','placeholder': 'Genre', 'required' : 'required' }),
            'img' : forms.TextInput({'class': 'form-control','placeholder': 'Nama file gambar', 'required' : 'required' })
        }

        
class formKoordinat(ModelForm):
    class Meta:
        model = Koordinat
        fields = '__all__'

        widgets = {
            'nama' : forms.TextInput({'class': 'form-control','placeholder': 'nama', 'required' : 'required' }),
            'koordinat' : forms.TextInput({'class': 'form-control','placeholder': 'koordinat', 'required' : 'required' }),
        }