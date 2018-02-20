from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views

# Create your views here.
def peringatan(request):
    return render(request,'karyawan/peringatan.html')

def tugas(request):
    return render(request,'karyawan/tugas.html')

def beranda(request):
    return render(request,'beranda/dasboard.html')