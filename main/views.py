from django.shortcuts import render

# Create your views here.
def aboutUs(request):
    return render(request,'about.html')

def electionOfficial(request):
    return render(request,"election-official.html")
def wardEmployee(request):
    return render(request,"ward-members.html")
def multipalStaffs(request):
    return render(request,"multipal-staffs.html")
