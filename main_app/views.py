from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Bird, Nest, Photo
from .forms import FeedingForm
import uuid
import boto3

S3_BASE_URL = 'https://s3.us-east-2.amazonaws.com/'
BUCKET = 'birdlog-django'

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def birds_index(request):
    birds = Bird.objects.filter(user=request.user)
    return render(request, 'birds/index.html', {
        'birds': birds,
    })

@login_required
def bird_detail(request, bird_id):
    bird = Bird.objects.get(id=bird_id)
    feeding_form = FeedingForm()

    bird_nest_material_ids = bird.nest_materials.all().values_list('id')
    nest_materials_bird_doesnt_have = Nest.objects.exclude(id__in=bird_nest_material_ids)

    return render(request, 'birds/detail.html', {
        'bird': bird,
        'feeding_form': feeding_form,
        'nest_materials': nest_materials_bird_doesnt_have,
    })

@login_required
def add_feeding(request, bird_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.bird_id = bird_id
        new_feeding.save()
    
    return redirect('bird_detail', bird_id=bird_id)

@login_required
def assoc_nest_material(request, bird_id, nest_material_id):
    Bird.objects.get(id=bird_id).nest_materials.add(nest_material_id)
    return redirect('bird_detail', bird_id=bird_id)

@login_required
def remove_assoc_nest_material(request, bird_id, nest_material_id):
    Bird.objects.get(id=bird_id).nest_materials.remove(nest_material_id)
    return redirect('bird_detail', bird_id=bird_id)

# URL /accounts/signup -- GET/POST
def signup(request):
    error_message = ''
    # POST request
    if request.method == 'POST':
        # create a user using the UserCreationForm -- this way we can validate the form
        form = UserCreationForm(request.POST)
        # check if the form inputs are valid
        if form.is_valid():
        # if valid; save new user to the database
            user = form.save()
            # login the new user
            login(request, user)
            # redirect to the cats index page
            return redirect('birds_index')
        else:
        # else: generate an error message -- 
            error_message = 'Invalid sign up - please try again'

    # GET requests
        # send an empty form to the client
    form = UserCreationForm()
    return render(request, 'registration/signup.html', { 
        'form': form, 
        'error': error_message
    })

def add_photo(request, bird_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f'{S3_BASE_URL}{BUCKET}/{key}'
            Photo.objects.create(url=url, bird_id=bird_id)
        except Exception as error:
            print('Photo upload failed')
            print(photo_file.name)
            print(key)
            print(error)
    return redirect('bird_detail', bird_id=bird_id)


class BirdCreate(LoginRequiredMixin, CreateView):
    model = Bird
    fields = ['species', 'date_observed', 'time_observed', 'location_observed', 'weather', 'number_observed', 'field_notes']
    template_name = 'birds/bird_form.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class BirdUpdate(LoginRequiredMixin, UpdateView):
    model = Bird
    fields = ['species', 'date_observed', 'time_observed', 'location_observed', 'weather', 'number_observed', 'field_notes']
    template_name = 'birds/bird_form.html'

class BirdDelete(LoginRequiredMixin, DeleteView):
    model = Bird
    success_url = '/birds/'
    template_name = 'birds/bird_confirm_delete.html'

class NestMaterialList(LoginRequiredMixin, ListView):
    model = Nest
    template_name = 'nest/nest_material_list.html'

class NestMaterialDetail(LoginRequiredMixin, DetailView):
    model = Nest
    template_name = 'nest/nest_material_detail.html'

class NestMaterialCreate(LoginRequiredMixin, CreateView):
    model = Nest
    fields = '__all__'
    template_name = 'nest/nest_material_form.html'

class NestMaterialUpdate(LoginRequiredMixin, UpdateView):
    model = Nest
    fields = '__all__'
    template_name = 'nest/nest_material_form.html'

class NestMaterialDelete(LoginRequiredMixin, DeleteView):
    model = Nest
    success_url = '/nest/'
    template_name = 'nest/nest_material_confirm_delete.html'