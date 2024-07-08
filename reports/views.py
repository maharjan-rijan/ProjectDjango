from django.shortcuts import render

# Create your views here.
def annualReports(request):
    return render(request,"annual-reports.html")
def monthlyReports(request):
    return render(request,"monthly-reports.html")
def publicHearing(request):
    return render(request,"public-hearing.html")