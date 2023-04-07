from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('birds/', views.birds_index, name='birds_index'),
    path('birds/<int:bird_id>/', views.bird_detail, name='bird_detail'),
    path('birds/create/', views.BirdCreate.as_view(), name='bird_create'),
    path('birds/<int:pk>/update/', views.BirdUpdate.as_view(), name='bird_update'),
    path('birds/<int:pk>/delete/', views.BirdDelete.as_view(), name='bird_delete'),
    path('nest/', views.NestMaterialList.as_view(), name='nest_material_list'),
    path('nest/<int:pk>/', views.NestMaterialDetail.as_view(), name='nest_material_detail'),
    path('nest/create/', views.NestMaterialCreate.as_view(), name='nest_material_create'),
    path('nest/<int:pk>/update/', views.NestMaterialUpdate.as_view(), name='nest_material_update'),
    path('nest/<int:pk>/delete/', views.NestMaterialDelete.as_view(), name='nest_material_delete'),
]