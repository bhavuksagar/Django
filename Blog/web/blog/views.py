from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from .models import art
# Create your views here.

class homePage(ListView):
    model =art
    template_name='index.html'
class detailPage(DetailView):
    model = art
    template_name='details.html'
    context_object_name = 'mod'
class editPage(UpdateView):
    model = art
    template_name='edit.html'
    fields='__all__'
    context_object_name = 'mod'
class Create(CreateView):
    model = art
    template_name='new.html'
    fields='__all__'
    context_object_name = 'mod'
