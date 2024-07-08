from django.urls import path
from .views import annualReports,monthlyReports,publicHearing
urlpatterns = [
    path('annual-reports/', annualReports, name="annual-reports"),
    path('monthly-reports/', monthlyReports, name="monthly-reports"),
    path('public-hearing/', publicHearing, name="public-hearing")
]
