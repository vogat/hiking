from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Trail
from django.views.generic.edit import CreateView, UpdateView, DeleteView


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def trails_index(request):
  trails = Trail.objects.all()
  return render(request, 'trails/index.html', {
    'trails': trails
  })

def trails_detail(request, trail_id):
  trail = Trail.objects.get(id=trail_id)
  return render (request, 'trails/detail.html', {'trail' : trail})

class TrailCreate(CreateView):
    model = Trail
    fields = '__all__'
    success_url = '/trails/'

class TrailUpdate(UpdateView):
  model = Trail
  fields = ['image', 'difficulty', 'description', 'streetAddress', 'city', 'state', 'zip', 'map']

class TrailDelete(DeleteView):
  model = Trail
  success_url = '/trails/'
