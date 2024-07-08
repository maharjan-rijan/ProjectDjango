from django.shortcuts import render
from main.models import About,Member
# Create your views here.
def aboutUs(request):
    aboutData=About.objects.all()
    memberData=Member.objects.all()
    data={
        'aboutData':aboutData,
        'memberData' : memberData
    }
    return render(request,'about.html',data)

def electionOfficial(request):
    return render(request,"election-official.html")
def wardEmployee(request):
    return render(request,"ward-members.html")
def multipalStaffs(request):
    return render(request,"multipal-staffs.html")
