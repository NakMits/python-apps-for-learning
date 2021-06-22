import os

from django.urls import reverse_lazy

from . import models

from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView


# Create your views here.


class IndexView(TemplateView):
    template_name = 'recomap/index.html'


class MapView(TemplateView):
    template_name = 'recomap/map.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["GOOGLEMAPS_APIKEY"] = os.environ['GOOGLEMAPS_APIKEY']
        return context


class MarkerReadListView(ListView):
    template_name = 'recomap/marker_read_list.html'
    model = models.MarkerModel


class MarkerReadDetailView(DetailView):
    template_name = 'recomap/marker_read_detail.html'
    model = models.MarkerModel


class MarkerCreateView(CreateView):
    template_name = 'recomap/marker_create.html'
    model = models.MarkerModel
    fields = ('title', 'tag', 'memo', 'lat', 'lng')
    success_url = reverse_lazy('recomap:marker_read_list')


class MarkerDeleteView(DeleteView):
    template_name = 'recomap/marker_delete.html'
    model = models.MarkerModel
    success_url = reverse_lazy('recomap:marker_read_list')


class MarkerUpdateView(UpdateView):
    template_name = 'recomap/marker_update.html'
    model = models.MarkerModel
    fields = ('title', 'tag', 'memo', 'lat', 'lng')
    success_url = reverse_lazy('recomap:marker_read_list')


