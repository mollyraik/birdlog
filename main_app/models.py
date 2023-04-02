from django.db import models
from django.utils import timezone
from datetime import datetime

def get_current_time():
    return datetime.now().time()

# Create your models here.
class Bird(models.Model):
    species = models.CharField(max_length=100)
    date_observed = models.DateField(default=timezone.now)
    time_observed = models.TimeField(default=get_current_time)
    location_observed = models.CharField(max_length=100)
    weather = models.CharField(max_length=100)
    number_observed = models.IntegerField(default=1)
    field_notes = models.TextField(max_length=250)

    def __str__(self):
        return self.species
