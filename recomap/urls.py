from django.urls import path
from . import views

app_name = 'recomap'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('helloworld', views.HelloWorldView.as_view(), name='helloworld'),
    path('map', views.MapView.as_view(), name='map'),
]