from django.http import HttpResponse
from django.shortcuts import render
def homePage(request):
    return render(request, "index.html")

def aboutUs(request):
    return render(request,"about.html")
def electionOfficial(request):
    return render(request,"election-official.html")
def wardEmployee(request):
    return render(request,"ward-members.html")
def multipalStaffs(request):
    return render(request,"multipal-staffs.html")

def programAndProjects(request):
    return render(request,"budget-program.html")
def planningAndProjects(request):
    return render(request,"planning-project.html")

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

def vitalRegister(request):
    return render(request,"vitalReg.html")
def socialSecurity(request):
    return render(request,"socialSecurity.html")
def citizenCharacter(request):
    return render(request,"citizenCharacter.html")
def applicationLetter(request):
    return render(request,"applicationLetter.html")

def publicHearing(request):
    return render(request,"public-hearing.html")
def annualReports(request):
    return render(request,"annual-reports.html")
def monthlyReports(request):
    return render(request,"monthly-reports.html")

def galleries(request):
    return render(request,"gallery.html")

def contact(request):
    return render(request,"contact.html")