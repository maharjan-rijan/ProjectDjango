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

def publicHearing(request):
    return render(request,"public-hearing.html")

def annualReports(request):
    return render(request,"annual-reports.html")

def monthlyReports(request):
    return render(request,"monthly-reports.html")

def programAndProjects(request):
    return render(request,"budget-program.html")

def planningAndProjects(request):
    return render(request,"planning-project.html")

def galleries(request):
    return render(request,"gallery.html")

def contact(request):
    return render(request,"contact.html")