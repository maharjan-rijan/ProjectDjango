from django.db import models

CATEGORY = (
    ("electionOfficial", "electionOfficial"),
    ("multipalStaffs", "multipalStaffs"),
    ("wardMembers", "wardMembers"),
)
POSITION = ( 
    ("mayor", "mayor"),
    ("deputy-mayor", "deputy-mayor"),
    ("Deputy Secretary", "Deputy Secretary"),
    ("Branch Officer","Branch Officer"),
    ("Accounts Officer","Accounts Officer"),
    ("engineer", "engineer"),
)
# Create your models here.
class About(models.Model):
    title=models.CharField(max_length=100,null=True,default=None)
    slug=models.SlugField(unique=True,null=True,default=None)
    contact=models.CharField(max_length=100,null=True)
    email=models.EmailField(max_length=300,null=True)
    description=models.TextField()
    
class Member(models.Model):
    category=models.CharField(max_length=50,choices=CATEGORY,default=None,null=True)
    name=models.CharField(max_length=100,default=None)
    slug=models.SlugField(unique=True,null=True,default=None)
    image=models.FileField(upload_to="staffs/",max_length=255,null=True,default=None)
    designation=models.CharField(max_length=100,default=None)
    contact=models.CharField(max_length=100,null=True)
    email=models.EmailField(max_length=300,null=True)
    position=models.CharField(max_length=50,choices=POSITION,default=None)