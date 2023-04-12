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
    path('birds/<int:bird_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('birds/<int:bird_id>/add_photo/', views.add_photo, name='add_photo'),
    path('nest/', views.NestMaterialList.as_view(), name='nest_material_list'),
    path('nest/<int:pk>/', views.NestMaterialDetail.as_view(), name='nest_material_detail'),
    path('nest/create/', views.NestMaterialCreate.as_view(), name='nest_material_create'),
    path('nest/<int:pk>/update/', views.NestMaterialUpdate.as_view(), name='nest_material_update'),
    path('nest/<int:pk>/delete/', views.NestMaterialDelete.as_view(), name='nest_material_delete'),
    path('birds/<int:bird_id>/assoc_nest_material/<int:nest_material_id>/', views.assoc_nest_material, name='assoc_nest_material'),
    path('birds/<int:bird_id>/assoc_nest_material/<int:nest_material_id>/remove', views.remove_assoc_nest_material, name='remove_assoc_nest_material'),
    path('accounts/signup/', views.signup, name='signup'),
]