from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HelloWorldView(TemplateView):
    template_name = 'recomap/helloworld.html'
