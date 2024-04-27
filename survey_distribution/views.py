# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Survey, Recipient


@login_required
def survey_distribution(request, survey_id):
    survey = get_object_or_404(Survey, id=survey_id)
    recipients = Recipient.objects.filter(survey=survey)

    return render(request, 'survey_distribution.html', {'survey': survey, 'recipients': recipients})


def survey_list(request):
    surveys = Survey.objects.all()
    return render(request, 'survey_list.html', {'surveys': surveys})
