from django.shortcuts import render

# Create your views here.
def newsNotice(request):
    return render(request,"newsNotice.html")