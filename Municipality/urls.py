"""
URL configuration for Municipality project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Municipality import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homePage, name='home'),
    path('about/',views.aboutUs, name='about'),
    path('contact/',views.contact, name='contact'),
    path('election-official/',views.electionOfficial, name='election-official'),
    path('ward-employee/',views.wardEmployee, name='ward-employee'),
    path('public-hearing/',views.publicHearing, name='public-hearing'),
    path('multipal-staffs/',views.multipalStaffs, name='multipal-staffs'),
    path('annual-reports/',views.annualReports, name='annual-reports'),
    path('monthly-reports/',views.monthlyReports, name='monthly-reports'),
    path('gallery/',views.galleries, name='gallery'),
    
    
]
