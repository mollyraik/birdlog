from django.contrib import admin

# Register your models here.
from .models import Bird, Nest

admin.site.register(Bird)
admin.site.register(Nest)