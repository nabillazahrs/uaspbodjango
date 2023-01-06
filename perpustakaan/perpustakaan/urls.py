"""perpustakaan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from perpus_app.views import* #* buat masukin semuanyaaa
from perpus_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('crudmainan/', crudmainan),
    path('crudpeta/', crudpeta),
    path("index/<int:id>", detail, name = 'detail'),
    path('tambah/', tambah),
    path("crudmainan/update/<int:id>", update, name = 'update'),
    path("crudmainan/delete/<int:id>", delete, name = 'delete'),
    path('login/',views.LoginPage,name='login'),
    path('signup/',views.SignupPage,name='signup'),
    path('login2/',views.Login2Page,name='login2'),
    path('signup2/',views.Signup2Page,name='signup2'),
]
