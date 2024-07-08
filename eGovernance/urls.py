from django.urls import path
from .views import vitalRegister,socialSecurity,citizenCharacter,applicationLetter
urlpatterns = [
   path('vital-registration/',vitalRegister, name='vital-reg'),
    path('social-security/',socialSecurity, name='social-security'),
    path('citizen-character/',citizenCharacter, name='citizen-character'),
    path('application-letter/',applicationLetter, name='application-letter'),
]