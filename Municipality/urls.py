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
from django.urls import path, include
from Municipality import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage, name='home'),
    path('about/',views.aboutUs, name='about'),
    path('election-official/',views.electionOfficial, name='election-official'),
    path('ward-employee/',views.wardEmployee, name='ward-employee'),
    path('multipal-staffs/',views.multipalStaffs, name='multipal-staffs'),
    
    path('budget-program/',views.programAndProjects, name='budget-program'),
    path('planning-project/',views.planningAndProjects, name='planning-project'),
    
    path('department-of-administration-planning-and-monitoring/',views.departofAdminPlan, name='doapam'),
    path('department-of-education/',views.departofEdu, name='doedu'),
    path('department-of-economic-administration/',views.departofEcoAdmin, name='doea'),
    path('department-of-infrastructure-development/',views.departofInfraDevlop, name='doid'),
    path('department-of-health-service/',views.departofHealthservice, name='dohs'),
    path('department-of-social-development/',views.departofSocialDevelop, name='dosd'),
    path('department-of-economic-development/',views.departofEcoDevelop, name='doed'),
    path('department-of-agricultural/',views.departofAgri, name='doa'),
    path('department-of-law/',views.departofLaw, name='dol'),
    
    path('vital-registration/',views.vitalRegister, name='vital-reg'),
    path('social-security/',views.socialSecurity, name='social-security'),
    path('citizen-character/',views.citizenCharacter, name='citizen-character'),
    path('application-letter/',views.applicationLetter, name='application-letter'),
    
    path('public-hearing/',views.publicHearing, name='public-hearing'),
    path('annual-reports/',views.annualReports, name='annual-reports'),
    path('monthly-reports/',views.monthlyReports, name='monthly-reports'),
    
    path('gallery/',views.galleries, name='gallery'),
    
    path('news-notice/',views.newsNotice, name='newsNotice'),
    
    path('contact/',views.contact, name='contact'),
    
    
]
