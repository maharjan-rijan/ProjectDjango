from django.shortcuts import render

# Create your views here.
def departofAdminPlan(request):
    return render(request,"dapm.html")
def departofEdu(request):
    return render(request,"dedu.html")
def departofEcoAdmin(request):
    return render(request,"dea.html")
def departofInfraDevlop(request):
    return render(request,"did.html")
def departofHealthservice(request):
    return render(request,"dhs.html")
def departofSocialDevelop(request):
    return render(request,"dsd.html")
def departofEcoDevelop(request):
    return render(request,"ded.html")
def departofAgri(request):
    return render(request,"da.html")
def departofLaw(request):
    return render(request,"dl.html")