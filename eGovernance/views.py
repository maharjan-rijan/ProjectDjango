from django.shortcuts import render

# Create your views here.
def vitalRegister(request):
    return render(request,"vitalReg.html")
def socialSecurity(request):
    return render(request,"socialSecurity.html")
def citizenCharacter(request):
    return render(request,"citizenCharacter.html")
def applicationLetter(request):
    return render(request,"applicationLetter.html")