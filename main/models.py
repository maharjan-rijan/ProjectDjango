from django.db import models

STAFFS = (
    ("electionOfficial", "electionOfficial"),
    ("multipalStaffs", "multipalStaffs"),
    ("wardMembers", "wardMembers"),
)
# Create your models here.
class About(models.Model):
    title=models.CharField(max_length=100,null=True,default=None)
    slug=models.SlugField(unique=True,null=True,default=None)
    contact=models.CharField(max_length=100,null=True)
    email=models.EmailField(max_length=300,null=True)
    description=models.TextField()
    
class Member(models.Model):
    name=models.CharField(max_length=100,default=None)
    slug=models.SlugField(unique=True,null=True,default=None)
    image=models.FileField(upload_to="staffs/",max_length=255,null=True,default=None)
    designation=models.CharField(max_length=100,default=None)
    contact=models.CharField(max_length=100,null=True)
    email=models.EmailField(max_length=300,null=True)
    memberOf=models.CharField(max_length=50,choices=STAFFS,default=None)