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
    memberData=Member.objects.all()
    data={
        'memberData' : memberData
    }
    return render(request,"election-official.html", data)
def wardEmployee(request):
    memberData=Member.objects.all()
    data={
        'memberData' : memberData
    }
    return render(request,"ward-members.html",data)
def multipalStaffs(request):
    memberData=Member.objects.all()
    data={
        'memberData' : memberData
    }
    return render(request,"multipal-staffs.html", data)
