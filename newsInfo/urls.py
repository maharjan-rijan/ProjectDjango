from django.urls import path
from .views import newsNotice
urlpatterns = [
   path('news-notice/',newsNotice, name='newsNotice'),
]
