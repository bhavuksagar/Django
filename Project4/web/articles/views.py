from django.views.generic import ListView

from .models import cnn
class homePage(ListView):
    model = cnn
    template_name="home.html"
