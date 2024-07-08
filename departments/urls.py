from django.urls import path
from .views import departofAdminPlan,departofEdu,departofEcoAdmin,departofInfraDevlop,departofHealthservice,departofSocialDevelop,departofEcoDevelop,departofAgri,departofLaw
urlpatterns = [
    path('department-of-administration-planning-and-monitoring/',departofAdminPlan, name='doapam'),
    path('department-of-education/',departofEdu, name='doedu'),
    path('department-of-economic-administration/',departofEcoAdmin, name='doea'),
    path('department-of-infrastructure-development/',departofInfraDevlop, name='doid'),
    path('department-of-health-service/',departofHealthservice, name='dohs'),
    path('department-of-social-development/',departofSocialDevelop, name='dosd'),
    path('department-of-economic-development/',departofEcoDevelop, name='doed'),
    path('department-of-agricultural/',departofAgri, name='doa'),
    path('department-of-law/',departofLaw, name='dol'),
]