from django.urls import path
from .views import *
urlpatterns = [
    path('about/', aboutUs, name="about"),
    path('election-official/',electionOfficial, name='election-official'),
    path('ward-employee/',wardEmployee, name='ward-employee'),
    path('multipal-staffs/',multipalStaffs, name='multipal-staffs'),
]

