from django.db import models
ProgramProj = (
    ("budgetProgram", "budgetProgram"),
    ("PlanningProject", "PlanningProject"),
)
# Create your models here.
class ProgramProject(models.Model):
    title=models.CharField(max_length=100,default=None)
    slug=models.SlugField(unique=True,null=True,default=None)
    file=models.FileField(upload_to="programProject/",max_length=255,null=True,default=None)
    dateTime=models.DateField()
    category=models.CharField(max_length=50,choices=ProgramProj,default=None)