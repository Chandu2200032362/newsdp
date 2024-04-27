# urls.py
from django.urls import path
from .views import survey_list, survey_distribution

urlpatterns = [
    path('surveys/', survey_list, name='survey_list'),
    path('survey_distribution', survey_distribution, name='survey_distribution'),
    # Add other URLs as needed
]
