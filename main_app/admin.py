from django.contrib import admin

# Register your models here.
from .models import Bird, Nest, Feeding, Photo

admin.site.register([Bird, Nest, Feeding, Photo])