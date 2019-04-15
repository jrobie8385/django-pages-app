from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class PreHomeView(TemplateView):
    template_name = "prehome.html"
