from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Sections(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title

class Articles(models.Model):
    title = models.CharField(max_length=64)
    sections = models.ForeignKey(Sections, on_delete=models.CASCADE)

    def __str__(self):
        return self.title