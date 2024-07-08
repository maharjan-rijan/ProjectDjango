from django.shortcuts import render

# Create your views here.
def programAndProjects(request):
    return render(request,"budget-program.html")
def planningAndProjects(request):
    return render(request,"planning-project.html")