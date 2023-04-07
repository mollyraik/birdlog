from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Bird, Nest

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def birds_index(request):
    birds = Bird.objects.all()
    return render(request, 'birds/index.html', {
        'birds': birds,
    })

def bird_detail(request, bird_id):
    bird = Bird.objects.get(id=bird_id)
    return render(request, 'birds/detail.html', {
        'bird': bird,
    })

class BirdCreate(CreateView):
    model = Bird
    fields = '__all__'
    template_name = 'birds/bird_form.html'

class BirdUpdate(UpdateView):
    model = Bird
    fields = '__all__'
    template_name = 'birds/bird_form.html'

class BirdDelete(DeleteView):
    model = Bird
    success_url = '/birds/'
    template_name = 'birds/bird_confirm_delete.html'

class NestMaterialList(ListView):
    model = Nest
    template_name = 'nest/nest_material_list.html'

class NestMaterialDetail(DetailView):
    model = Nest
    template_name = 'nest/nest_material_detail.html'

class NestMaterialCreate(CreateView):
    model = Nest
    fields = '__all__'
    template_name = 'nest/nest_material_form.html'

class NestMaterialUpdate(UpdateView):
    model = Nest
    fields = '__all__'
    template_name = 'nest/nest_material_form.html'

class NestMaterialDelete(DeleteView):
    model = Nest
    success_url = '/nest/'
    template_name = 'nest/nest_material_confirm_delete.html'