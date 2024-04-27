from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.shortcuts import render

# Create your views here.
class Review(models.Model):
    user = models.CharField(max_length=100)
    text = models.TextField()
    rating = models.IntegerField()
    image = models.ImageField(upload_to='D:\MY PROJECT\E_Survey\static\Images\565.jpg', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f'Review - {self.created_at}'

from django.db import models

# Create your models here.