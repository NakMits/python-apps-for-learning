import os

from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class IndexView(TemplateView):
    template_name = 'recomap/index.html'

class HelloWorldView(TemplateView):
    template_name = 'recomap/helloworld.html'

class MapView(TemplateView):
    template_name = 'recomap/map.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["GOOGLEMAPS_APIKEY"] = os.environ['GOOGLEMAPS_APIKEY']
        return context
