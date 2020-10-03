from django.views.generic import TemplateView

class homePage(TemplateView):
    template_name="index.html"

class aboutPage(TemplateView):
    template_name = "about.html"

class contactPage(TemplateView):
    template_name = "con.html"
