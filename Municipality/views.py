from django.http import HttpResponse
from django.shortcuts import render
from main.models import *

def homePage(request):
    aboutData=About.objects.all()
    memberData=Member.objects.all()
    data={
        'aboutData':aboutData,
        'memberData' : memberData
    }
    return render(request,'index.html',data)

def galleries(request):
    return render(request,"gallery.html")

def contact(request):
    return render(request,"contact.html")