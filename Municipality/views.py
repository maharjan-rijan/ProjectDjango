from django.http import HttpResponse
from django.shortcuts import render
def homePage(request):
    return render(request, "index.html")

def aboutUs(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")