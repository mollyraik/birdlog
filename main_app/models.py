from django.db import models
from django.utils import timezone
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User

def get_current_time():
    return datetime.now().time()

# Create your models here.
class Nest(models.Model):
    item = models.CharField(max_length=50)
    material = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('nest_material_detail', kwargs={'pk': self.id})


class Bird(models.Model):
    species = models.CharField(max_length=100)
    date_observed = models.DateField(default=timezone.now)
    time_observed = models.TimeField(default=get_current_time)
    location_observed = models.CharField(max_length=100)
    weather = models.CharField(max_length=100)
    number_observed = models.IntegerField(default=1)
    field_notes = models.TextField(max_length=250)
    nest_materials = models.ManyToManyField(Nest)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.species
    
    def get_absolute_url(self):
        return reverse('bird_detail', kwargs={ 'bird_id': self.id })
    
class Feeding(models.Model):
    TYPES = (
        ('I', 'Insects'),
        ('S', 'Seeds'),
        ('B', 'Berries'),
        ('F', 'Fish'),
        ('R', 'Rodents'),
    )
    date = models.DateField(default=timezone.now)
    type = models.CharField(max_length=1, choices=TYPES, default=TYPES[0][0])
    bird = models.ForeignKey(Bird, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_type_display()} on {self.date}'
    
    class Meta:
        ordering = ['-date']

class Photo(models.Model):
    url = models.CharField(max_length=200)
    bird = models.ForeignKey(Bird, on_delete=models.CASCADE)

    def __str__(self):
        return f'Photo for bird_id: {self.bird_id} @{self.url}'
    