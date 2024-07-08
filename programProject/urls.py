from django.urls import path
from .views import programAndProjects,planningAndProjects
urlpatterns = [
   path('budget-program/',programAndProjects, name='budget-program'),
    path('planning-project/',planningAndProjects, name='planning-project'),
]
