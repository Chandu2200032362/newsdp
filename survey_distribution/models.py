# models.py
from django.db import models
from django.contrib.auth.models import User

class Survey(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    # Add other survey-related fields as needed

    def __str__(self):
        return self.title

class Recipient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.survey.title}"
