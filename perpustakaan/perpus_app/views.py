from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from perpus_app.forms import FormBuku, formKoordinat

def index(request):
    books = Buku.objects.all()
    data = {
        'Title' : "Index",
        'Heading' : "Daftar Permainan Tradisional",
        'books' : books,
    }
    return render(request, 'index.html', data)

@login_required(login_url='login')
def crudmainan(request):
    books = Buku.objects.all()
    data = {
        'Title' : "Home",
        'Heading' : "CRUD Data Permainan",
        'books' : books,
    }
    return render(request, 'crudmainan.html' , data)

def tambah(request):
    if request.POST:
        form = FormBuku(request.POST)
        if form.is_valid():
            form.save()
            form = FormBuku()
            judul = 'Tambahkan Library Anda'
            pesan = 'Data Berhasil Ditambahkan!'
            data ={
        'title' : judul,
        'heading' : judul,
        'form' : form,
        'pesan' : pesan
    }
        return render(request, 'tambah.html', data)
    else:
        form = FormBuku()
        films = Buku.objects.all()
        data ={
        'title' : 'Tambahkan Library Anda',
        'heading' : 'tambah data',
        'form' : form,
    }
    return render(request, 'tambah.html', data)

def update(request, id):
    books = Buku.objects.get(id = id)
    judul = "Update Library"
    template = "update.html"
    if request.POST:
        form = FormBuku(request.POST, instance=books)
        if form.is_valid():
            form.save()
            pesan = "Data Anda Sudah Diupdate"
            data ={
            'title' : judul,
            'heading' : judul,
            'pesan' : pesan,
            'books' : books,

    }
        return render(request, template, data)
    else:
        form = FormBuku(instance=books)
        data ={
        'title' : judul,
        'heading' : judul,
        'form' : form,
        'books' : books,
    }
    return render(request, template, data)

   
def delete(request, id):
    books = Buku.objects.get(id = id)
    books.delete()

    return redirect('/crudmainan/')


def crudpeta(request):
    if request.POST:
        form = formKoordinat(request.POST)
        if form.is_valid():
            form.save()
            form = formKoordinat()
            judul = 'Tambah Data Koordinat'
            pesan = 'Data Berhasil Ditambahkan!'
            data ={
        'title' : judul,
        'heading' : judul,
        'form' : form,
        'pesan' : pesan
    }
        return render(request, 'crudpeta.html', data)
    else:
        form = formKoordinat()
        Koordinats = Koordinat.objects.all()
        data ={
        'title' : 'Tambah Data Jurnal',
        'heading' : 'Tambah Data Jurnal',
        'form' : form,
        'Koordinats' : Koordinats,
    }
    return render(request, 'crudpeta.html', data)

def detail(request, id):
    detail = Buku.objects.get(pk=id)
    data = {
        'Title' : 'List Library',
        'detail' : detail,
    }
    return render(request, 'detail.html', data)

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('/crudmainan/')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    return render (request,'signup.html')

def Login2Page(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('/crudpeta/')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login2.html')

def Signup2Page(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login2')
    return render (request,'signup2.html')



# Create your views here.
