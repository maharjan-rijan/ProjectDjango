from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    return render(request,'index.html')

def galleries(request):
    return render(request,"gallery.html")

def contact(request):
    return render(request,"contact.html")