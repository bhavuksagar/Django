from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from .models import ArtModel
from django.urls import reverse_lazy
# Create your views here.
class homePage(ListView):
    model= ArtModel
    template_name='home.html'

class detailPage(DetailView):
    model= ArtModel
    template_name = 'detail.html'
    context_object_name ="bat"

class createview(CreateView):
    model = ArtModel
    template_name = 'new.html'
    fields= '__all__'
class edit(UpdateView):
    model = ArtModel
    template_name = 'edit.html'
    fields= ['title','text']

class delete(DeleteView):
    model= ArtModel
    template_name = 'delete.html'
    success_url = reverse_lazy('homepage')
    context_object_name ="bat"
