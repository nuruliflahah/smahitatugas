from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')

def Datadirisiswa(request):
    return render(request,'Datadirisiswa.html')

def Dataorangtua(request):
    return render(request,'Dataorangtua.html') 


 