from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # path('birds/', views.birds_index, name='birds_index'),
    # path('birds/<int:bird_id>/', views.bird_detail, name='bird_detail'),
]